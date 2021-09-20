from typing import Any
from typing import List
from typing import Optional
from typing import Union

from brownie import *
from brownie.network.account import Account

from badger_utils.constants import WhaleRegistryAction
from badger_utils.registry import registry
from badger_utils.token_utils.balances import Balances


def get_token_balances(tokens: List[Any], accounts_to_check: List[Account]) -> Balances:
    balances = Balances()
    for token in tokens:
        for account in accounts_to_check:
            balances.set(token, account, token.balanceOf(account))
    return balances


def distribute_from_whale(
        whale_config, recipient: Account,
        percentage: Optional[float] = 0.2) -> None:
    if whale_config.action == WhaleRegistryAction.DISTRIBUTE_FROM_CONTRACT:
        force_ether = ForceEther.deploy({"from": recipient})
        if recipient.balance() < 2 * 10 ** 18:
            distribute_test_ether(recipient, Wei("2 ether"))
        recipient.transfer(force_ether, Wei("2 ether"))
        force_ether.forceSend(whale_config.whale, {"from": recipient})

    token = interface.IERC20(whale_config.token)
    token.transfer(
        recipient,
        token.balanceOf(whale_config.whale) * percentage,
        {"from": whale_config.whale},
    )


def distribute_from_whales(
        recipient: Account,
        percentage: Optional[float] = 0.8, assets: Union[Optional[str], List[str]] = "All") -> None:

    accounts[0].transfer(recipient, Wei("50 ether"))
    # Normal Transfers
    for key, whale_config in registry.whales.items():
        if assets != "All" and key not in assets:
            continue
        # Handle special cases after all standard distributions
        if whale_config.special:
            continue
        if key != "_pytestfixturefunction":
            distribute_from_whale(whale_config, recipient, percentage=percentage)


def distribute_test_ether(recipient: Account, amount: int) -> None:
    """
    On test environments, transfer ETH from default ganache account to specified account
    """
    idx = 0
    while idx < len(accounts):
        if accounts[idx].balance() >= amount:
            break
        idx += 1
    if idx != len(accounts):
        accounts[idx].transfer(recipient, amount)
