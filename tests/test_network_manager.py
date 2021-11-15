import pytest

from badger_utils.network_manager import ARBITRUM_NETWORK
from badger_utils.network_manager import BINANCE_NETWORK
from badger_utils.network_manager import ETHEREUM_NETWORK
from badger_utils.network_manager import POLYGON_NETWORK
from badger_utils.network_manager import network_manager


def test_network_manager_get_active_network__eth(mocker):
    mocker.patch(
        "badger_utils.network_manager.network.show_active",
        return_value="mainnet"
    )
    assert network_manager.get_active_network() == ETHEREUM_NETWORK


def test_network_manager_get_active_network__polygon(mocker):
    mocker.patch(
        "badger_utils.network_manager.network.show_active",
        return_value="polygon"
    )
    assert network_manager.get_active_network() == POLYGON_NETWORK


def test_network_manager_get_active_network__arbitrum(mocker):
    mocker.patch(
        "badger_utils.network_manager.network.show_active",
        return_value="arbitrum"
    )
    assert network_manager.get_active_network() == ARBITRUM_NETWORK


def test_network_manager_get_active_network__binance(mocker):
    mocker.patch(
        "badger_utils.network_manager.network.show_active",
        return_value="bsc"
    )
    assert network_manager.get_active_network() == BINANCE_NETWORK


def test_network_manager_get_active_network__default():
    assert network_manager.get_active_network() == "development"


def test_network_manager_get_badger_deploy__eth(mocker):
    mocker.patch(
        "badger_utils.network_manager.network.show_active",
        return_value="mainnet"
    )
    assert network_manager.get_active_network_badger_deploy() == 'deploy-final.json'


def test_network_manager_get_active_network__development(mocker):
    mocker.patch(
        "badger_utils.network_manager.network.show_active",
        return_value="development"
    )
    assert network_manager.get_active_network() == "development"


def test_network_manager_get_badger_deploy__binance(mocker):
    mocker.patch(
        "badger_utils.network_manager.network.show_active",
        return_value="bsc"
    )
    assert network_manager.get_active_network_badger_deploy() == 'badger-deploy-bsc.json'
