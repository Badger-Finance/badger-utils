import pytest
from brownie import BadgerRegistry  # noqa
from brownie import accounts

from badger_utils.constants import ETHEREUM_NETWORK
from badger_utils.registry import chain_registries


@pytest.mark.parametrize(
    "network",
    [
        "eth", "polygon", "arbitrum",
    ]
)
def test_get_all_registries(isolate, badger_registry, mocker, network):
    mocker.patch(
        "badger_utils.registry.on_chain_registries.BADGER_REGISTRY_ADDRESS",
        badger_registry.address,
    )
    chain_registries.initialize()
    assert chain_registries.get_registry(network) is not None


@pytest.mark.parametrize(
    "network",
    [
        "mainnet", "polygon", "arbitrum",
    ]
)
def test_get_active_registry(isolate, badger_registry, mocker, network):
    mocker.patch(
        "badger_utils.network_manager.network.show_active",
        return_value=network,
    )
    mocker.patch(
        "badger_utils.registry.on_chain_registries.BADGER_REGISTRY_ADDRESS",
        badger_registry.address,
    )
    chain_registries.initialize()
    assert chain_registries.get_active_chain_registry() is not None


def test_get_key_value_from_registry(isolate, badger_registry, mocker):
    # Deploy badger registry
    mocker.patch(
        "badger_utils.registry.on_chain_registries.BADGER_REGISTRY_ADDRESS",
        badger_registry.address,
    )
    chain_registries.initialize()
    badger_registry.initialize(accounts[0], {'from': accounts[0]})
    # Populate with some random address value
    badger_registry.set(
        "badgerTree", "0x635EB2C39C75954bb53Ebc011BDC6AfAAcE115A6",
        {'from': accounts[0]},
    )
    eth_registry = chain_registries.get_registry(ETHEREUM_NETWORK)
    assert eth_registry.get("badgerTree") == "0x635EB2C39C75954bb53Ebc011BDC6AfAAcE115A6"
