import pytest
import responses
from brownie import accounts
from brownie.network.account import Account

from badger_utils.token_utils.distribute_from_whales_realtime import distribute_from_whales_realtime
from badger_utils.utils import approx


@responses.activate
def test_distribute_from_whales_realtime(token, mock_target_tokens):
    responses.add(
        responses.PassthroughResponse(responses.POST, "http://127.0.0.1:8545/")
    )

    responses.add(
        responses.GET,
        f"https://api.ethplorer.io/getTopTokenHolders/{token.address}",
        json={'holders': [
            {
                'address': '0x19d099670a21bC0a8211a89B84cEdF59AbB4377F',
                'balance': 7.35e+24,
                'share': 35
            }]},
        status=200
    )
    initial_whale_balance = 100000
    initial_whale_eth = Account("0x19d099670a21bC0a8211a89B84cEdF59AbB4377F").balance()
    assert initial_whale_eth == 0
    token.transfer(
        "0x19d099670a21bC0a8211a89B84cEdF59AbB4377F", initial_whale_balance, {'from': accounts[0]}
    )
    distribute_from_whales_realtime(accounts[1], percentage=0.8)
    # Make sure that whale's address was topped
    assert Account("0x19d099670a21bC0a8211a89B84cEdF59AbB4377F").balance() != initial_whale_eth
    assert token.balanceOf(
        "0x19d099670a21bC0a8211a89B84cEdF59AbB4377F") == initial_whale_balance * 0.2
    assert token.balanceOf(accounts[1].address) == initial_whale_balance * 0.8


@responses.activate
def test_distribute_from_whales_realtime__recipient_address_topped(token, mock_target_tokens):
    responses.add(
        responses.PassthroughResponse(responses.POST, "http://127.0.0.1:8545/")
    )

    responses.add(
        responses.GET,
        f"https://api.ethplorer.io/getTopTokenHolders/{token.address}",
        json={'holders': [
            {
                'address': '0x19d099670a21bC0a8211a89B84cEdF59AbB4377F',
                'balance': 7.35e+24,
                'share': 35
            }]},
        status=200
    )
    token.transfer(
        "0x19d099670a21bC0a8211a89B84cEdF59AbB4377F", 123, {'from': accounts[0]}
    )
    # Burn ether to chech that function will top up eth balance
    accounts[7].transfer(accounts[1], "100 ether", gas_price=0)
    assert accounts[7].balance() == 0
    distribute_from_whales_realtime(accounts[7], percentage=0.8)
    assert approx(accounts[7].balance(), 47999999999999863990, 99)


@responses.activate
def test_distribute_from_whales_realtime__recipient_address_not_topped(token, mock_target_tokens):
    responses.add(
        responses.PassthroughResponse(responses.POST, "http://127.0.0.1:8545/")
    )

    responses.add(
        responses.GET,
        f"https://api.ethplorer.io/getTopTokenHolders/{token.address}",
        json={'holders': [
            {
                'address': '0x19d099670a21bC0a8211a89B84cEdF59AbB4377F',
                'balance': 7.35e+24,
                'share': 35
            }]},
        status=200
    )
    token.transfer(
        "0x19d099670a21bC0a8211a89B84cEdF59AbB4377F", 123, {'from': accounts[0]}
    )
    # Burn ether to check that function will top up eth balance
    accounts[7].transfer(accounts[1], "100 ether", gas_price=0)
    assert accounts[7].balance() == 0
    # Cannot call distribute from whales since account has not enough balance
    with pytest.raises(ValueError):
        distribute_from_whales_realtime(accounts[7], percentage=0.8)
