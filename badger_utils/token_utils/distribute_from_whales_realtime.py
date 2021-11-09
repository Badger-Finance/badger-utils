from typing import List
from typing import Optional
from typing import Union

from brownie import *
from brownie.network.account import Account

from badger_utils.constants import TARGET_TOKENS
from badger_utils.ethplorer_utils import get_top_token_holders
from badger_utils.token_utils.utils import distribute_test_ether
from badger_utils.utils import is_address_eoa


class TokenWhaleNotFound(Exception):
    pass


def distribute_from_whale_realtime(
        token_address: str, recipient: Account,
        percentage: Optional[float] = 0.2) -> None:
    token_whales = get_top_token_holders(token_address)['holders']
    target_whale = ''
    for token_whale in token_whales:
        # Use first whale that is not a contract
        if is_address_eoa(web3.toChecksumAddress(token_whale['address'])):
            target_whale = token_whale['address']  # type: str
    if not target_whale:
        raise TokenWhaleNotFound(f"Cannot find whale for token {token_address}")
    force_ether = ForceEther.deploy({"from": recipient})
    if recipient.balance() < 2 * 10 ** 18:
        distribute_test_ether(recipient, Wei("2 ether"))
    recipient.transfer(force_ether, Wei("2 ether"))
    force_ether.forceSend(target_whale, {"from": recipient})

    token = interface.IERC20(token_address)
    token.transfer(
        recipient,
        token.balanceOf(target_whale) * percentage,
        {"from": target_whale},
    )


def distribute_from_whales_realtime(
        recipient: Account,
        percentage: Optional[float] = 0.8, assets: Union[Optional[str], List[str]] = "All",
        tokens: Optional[List[str]] = None) -> None:
    """
    NOTE: This only works on Ethereum, since Ethplorer doesn't support any other chain
    """
    if not tokens:
        tokens = TARGET_TOKENS
    # Normal Transfers
    for token_addr in tokens:
        if assets != "All":
            continue
        distribute_from_whale_realtime(token_addr, recipient, percentage=percentage)
