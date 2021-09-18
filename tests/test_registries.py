from badger_utils.network_manager import ETHEREUM_NETWORK
from badger_utils.network_manager import BINANCE_NETWORK
from badger_utils.registry import registries


def test_eth_registry_present():
    eth_registry = registries.get_registry(ETHEREUM_NETWORK)
    assert eth_registry.aave
    assert eth_registry.aragon
    assert eth_registry.badger
    assert eth_registry.chainlink
    assert eth_registry.compound
    assert eth_registry.convex
    assert eth_registry.curve
    assert eth_registry.gnosis_safe
    assert eth_registry.sushiswap
    assert eth_registry.uniswap


def test_bsc_registry_present():
    bsc_registry = registries.get_registry(BINANCE_NETWORK)
    assert bsc_registry.sushiswap
    assert bsc_registry.sushi
    assert bsc_registry.multicall
    assert bsc_registry.pancake
    assert bsc_registry.tokens


def test_get_current_registry__bsc(mocker):
    mocker.patch(
        "badger_utils.network_manager.network.show_active",
        return_value="bsc"
    )
    bsc_registry = registries.get_active_chain_registry()
    assert registries.registries['bsc'] == bsc_registry


def test_get_current_registry__eth(mocker):
    mocker.patch(
        "badger_utils.network_manager.network.show_active",
        return_value="mainnet"
    )
    eth_registry = registries.get_active_chain_registry()
    assert registries.registries['eth'] == eth_registry
