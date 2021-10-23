import pytest
import responses
from requests import HTTPError

from badger_utils.gas_utils.gas_now_compatible_strategy import GasNowCompatibleStrategy

ETHERCHAIN_GASNOW_API_RESPONSE = {
    "code": 200,
    "data": {
        "rapid": 167008603024,
        "fast": 123200000000,
        "standard": 105000000000,
        "slow": 80466186189,
        "timestamp": 1634834908855,
        "priceUSD": 4078.94
    }
}


@pytest.mark.parametrize("speed", ["rapid", "fast", "slow", "standard"])
@responses.activate
def test_gas_now_compatible_happy_path(speed):
    responses.add(
        responses.GET, "https://etherchain.org/api/gasnow",
        json=ETHERCHAIN_GASNOW_API_RESPONSE, status=200
    )
    strategy = GasNowCompatibleStrategy(speed)
    assert strategy.get_gas_price() == ETHERCHAIN_GASNOW_API_RESPONSE['data'][speed]


@responses.activate
def test_gas_now_compatible_unhappy_path():
    responses.add(
        responses.GET, "https://etherchain.org/api/gasnow",
        json={}, status=404
    )
    with pytest.raises(HTTPError):
        GasNowCompatibleStrategy("fast").get_gas_price()


def test_gas_now_compatible_invalid_speed():
    with pytest.raises(ValueError):
        GasNowCompatibleStrategy("invalid")
