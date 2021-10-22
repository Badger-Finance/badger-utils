import responses

from badger_utils.gas_utils import GasStrategies
from badger_utils.gas_utils.gas_utils import StaticGasStrategy


@responses.activate
def test_gas_strategies__class_init():
    responses.add(
        responses.GET, "https://etherchain.org/api/gasnow",
        json={
            "code": 200,
            "data": {
                "rapid": 167008603024,
                # Fast is the gas speed that is used in gas cost computations
                "fast": 147008603021,
                "standard": 105000000000,
                "slow": 80466186189,
                "timestamp": 1634834908855,
                "priceUSD": 4078.94
            }
        }, status=200
    )
    stragegies = GasStrategies()
    assert stragegies.standard is not None
    assert stragegies.fast is not None
    assert stragegies.rapid is not None
    assert stragegies.bsc_static is not None
    assert stragegies.exponential_scaling is not None
    assert stragegies.exponential_scaling_fast is not None


@responses.activate
def test_optimal_price__takes_minimal_price():
    responses.add(
        responses.GET, "https://etherchain.org/api/gasnow",
        json={
            "code": 200,
            "data": {
                "rapid": 167008603024,
                # Fast is the gas speed that is compared to analyzed.mode value
                "fast": 123123,
                "standard": 105000000000,
                "slow": 80466186189,
                "timestamp": 1634834908855,
                "priceUSD": 4078.94
            }
        }, status=200
    )
    stragegies = GasStrategies()
    price = stragegies.optimal_price()
    assert price == 123123


@responses.activate
def test_gas_gost():
    responses.add(
        responses.GET, "https://etherchain.org/api/gasnow",
        json={
            "code": 200,
            "data": {
                "rapid": 167008603024,
                # Fast is the gas speed that is used in gas cost computations
                "fast": 123123,
                "standard": 105000000000,
                "slow": 80466186189,
                "timestamp": 1634834908855,
                "priceUSD": 4078.94
            }
        }, status=200
    )
    stragegies = GasStrategies()
    price = stragegies.gas_cost(21000)
    assert price == 123123 * 21000


@responses.activate
def test_set_default_strategy(mocker):
    mocker.patch(
        "badger_utils.network_manager.network.show_active",
        return_value="mainnet"
    )
    gas_price = mocker.patch(
        "badger_utils.gas_utils.gas_utils.gas_price",
    )
    responses.add(
        responses.GET, "https://etherchain.org/api/gasnow",
        json={
            "code": 200,
            "data": {
                "rapid": 167008603024,
                "fast": 123123,
                "standard": 105000000000,
                "slow": 80466186189,
                "timestamp": 1634834908855,
                "priceUSD": 4078.94
            }
        }, status=200
    )
    stragegies = GasStrategies()
    stragegies.set_default_for_active_chain()
    assert gas_price.called


def test_static_gas_strategy():
    static_strategy = StaticGasStrategy(price=123)
    assert static_strategy.get_gas_price() == 123
