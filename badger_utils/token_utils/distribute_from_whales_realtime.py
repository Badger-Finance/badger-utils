import os
from time import sleep
from typing import List
from typing import Optional
from typing import Union

from brownie import *
from brownie.network.account import Account

from badger_utils.constants import TARGET_TOKENS
from badger_utils.ethplorer_utils import get_top_token_holders
from badger_utils.utils import is_address_eoa


class TokenWhaleNotFound(Exception):
    pass


class NotEnoughBalance(Exception):
    pass


def _get_whale(token_addr: str) -> str:
    token_whales = get_top_token_holders(token_addr)['holders']
    target_whale = ''
    for token_whale in token_whales:
        # Use first whale that is not a contract
        if is_address_eoa(web3.toChecksumAddress(token_whale['address'])):
            target_whale = token_whale['address']  # type: str
            break
    if not target_whale:
        raise TokenWhaleNotFound(f"Cannot find whale for token {token_addr}")
    return target_whale


def _top_up_whale_with_funds(from_account: Account, whale: str):
    force_ether = ForceEther.deploy({"from": from_account})
    from_account.transfer(force_ether, Wei("2 ether"))
    force_ether.forceSend(whale, {"from": from_account})


def distribute_from_whales_realtime(
        recipient: Account,
        mantissa: Optional[Union[float, int]] = 0.8,
        tokens: Optional[List[str]] = None,
        percentage: Optional[bool] = True,
) -> None:
    """
    NOTE: This only works on Ethereum, since Ethplorer doesn't support any other chain
    """
    if not tokens:
        tokens = TARGET_TOKENS
    # Normal Transfers
    for token_addr in tokens:
        token = interface.IERC20(token_addr)
        target_whale = _get_whale(token_addr)
        _top_up_whale_with_funds(recipient, target_whale)
        if percentage:
            amount = token.balanceOf(target_whale) * mantissa
        else:
            amount = mantissa
        if token.balanceOf(target_whale) < amount:
            raise NotEnoughBalance(f"Whale {target_whale} has not enough balance")
        token.transfer(
            recipient, amount, {"from": target_whale}
        )
        # This is needed because Ethplrorer API will raise exc if requests are made too often
        # for the free API key
        if not os.environ.get('ETHPLORER_API_KEY'):
            sleep(0.5)


def distribute_from_whales_realtime_exact(
        recipient: Account, amount: int,
        tokens: Optional[List[str]] = None,
):
    distribute_from_whales_realtime(recipient, amount, tokens, percentage=False)


def distribute_from_whales_realtime_percentage(
        recipient: Account, percentage: float,
        tokens: Optional[List[str]] = None,
):
    distribute_from_whales_realtime(recipient, percentage, tokens, percentage=True)
