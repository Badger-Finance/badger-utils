import pytest

from utils.network_manager import ETHEREUM_NETWORK
from utils.network_manager import BINANCE_NETWORK
from utils.network_manager import network_manager


def test_network_manager_get_active_network__eth(mocker):
    mocker.patch(
        "utils.network_manager.network.show_active",
        return_value="mainnet"
    )
    assert network_manager.get_active_network() == ETHEREUM_NETWORK


def test_network_manager_get_active_network__binance(mocker):
    mocker.patch(
        "utils.network_manager.network.show_active",
        return_value="bsc"
    )
    assert network_manager.get_active_network() == BINANCE_NETWORK


def test_network_manager_get_active_network__not_recognized():
    with pytest.raises(Exception):
        network_manager.get_active_network()


def test_network_manager_get_badger_deploy__eth(mocker):
    mocker.patch(
        "utils.network_manager.network.show_active",
        return_value="mainnet"
    )
    assert network_manager.get_active_network_badger_deploy() == 'deploy-final.json'


def test_network_manager_get_badger_deploy__binance(mocker):
    mocker.patch(
        "utils.network_manager.network.show_active",
        return_value="bsc"
    )
    assert network_manager.get_active_network_badger_deploy() == 'badger-deploy-bsc.json'
