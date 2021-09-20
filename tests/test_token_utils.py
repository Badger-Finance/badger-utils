import pytest
from brownie import accounts
from brownie.network.account import Account
from dotmap import DotMap

from badger_utils.constants import WhaleRegistryAction
from badger_utils.token_utils import distribute_from_whales
from badger_utils.token_utils import get_token_balances
from badger_utils.utils import approx


def test_distribute_from_whales(token, mocker):
    initial_whale_balance = 100000
    initial_whale_eth = Account("0x19d099670a21bC0a8211a89B84cEdF59AbB4377F").balance()
    assert initial_whale_eth == 0
    token.transfer(
        "0x19d099670a21bC0a8211a89B84cEdF59AbB4377F", initial_whale_balance, {'from': accounts[0]}
    )
    mock_registry = DotMap(
        whales=DotMap(
            badger=DotMap(
                whale="0x19d099670a21bC0a8211a89B84cEdF59AbB4377F",
                token=token.address,
                action=WhaleRegistryAction.DISTRIBUTE_FROM_CONTRACT,
            ),
        ),
    )
    mocker.patch(
        "badger_utils.token_utils.utils.registry",
        mock_registry
    )
    distribute_from_whales(accounts[1], percentage=0.8)

    # Make sure that whale's address was topped
    assert Account("0x19d099670a21bC0a8211a89B84cEdF59AbB4377F").balance() != initial_whale_eth

    # Make sure only 20% of whale balance left and 80% are sent to recipient
    assert token.balanceOf(
        "0x19d099670a21bC0a8211a89B84cEdF59AbB4377F") == initial_whale_balance * 0.2

    assert token.balanceOf(accounts[1].address) == initial_whale_balance * 0.8


def test_distribute_from_whales__recipient_address_topped(token, mocker):
    token.transfer(
        "0x19d099670a21bC0a8211a89B84cEdF59AbB4377F", 123, {'from': accounts[0]}
    )
    mock_registry = DotMap(
        whales=DotMap(
            badger=DotMap(
                whale="0x19d099670a21bC0a8211a89B84cEdF59AbB4377F",
                token=token.address,
                action=WhaleRegistryAction.DISTRIBUTE_FROM_CONTRACT,
            ),
        ),
    )
    mocker.patch(
        "badger_utils.token_utils.utils.registry",
        mock_registry
    )
    # Burn ether to chech that function will top up eth balance
    accounts[7].transfer(accounts[1], "100 ether", gas_price=0)
    assert accounts[7].balance() == 0
    distribute_from_whales(accounts[7], percentage=0.8)
    assert approx(accounts[7].balance(), 47999999999999863990, 99)


def test_distribute_from_whales__recipient_address_not_topped(token, mocker):
    token.transfer(
        "0x19d099670a21bC0a8211a89B84cEdF59AbB4377F", 123, {'from': accounts[0]}
    )
    mock_registry = DotMap(
        whales=DotMap(
            badger=DotMap(
                whale="0x19d099670a21bC0a8211a89B84cEdF59AbB4377F",
                token=token.address,
                action=WhaleRegistryAction.DISTRIBUTE_FROM_EOA,
            ),
        ),
    )
    mocker.patch(
        "badger_utils.token_utils.utils.registry",
        mock_registry
    )
    # Burn ether to chech that function will top up eth balance
    accounts[7].transfer(accounts[1], "100 ether", gas_price=0)
    assert accounts[7].balance() == 0
    # Cannot call distribute from whales since account has not enough balance and it will not be
    # topped
    with pytest.raises(ValueError):
        distribute_from_whales(accounts[7], percentage=0.8)


def test_get_token_balance__zero(token):
    balances = get_token_balances([token], accounts_to_check=[accounts[5]])
    assert balances.get(token.address, accounts[5].address) == 0


def test_get_token_balance(token):
    token.transfer(accounts[2], 123, {'from': accounts[0]})
    balances = get_token_balances([token], accounts_to_check=[accounts[2]])
    assert balances.get(token.address, accounts[2].address) == 123
