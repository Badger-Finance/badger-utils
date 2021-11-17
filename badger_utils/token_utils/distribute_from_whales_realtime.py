from time import sleep
from typing import List
from typing import Optional

from brownie import *
from brownie.network.account import Account

from badger_utils.constants import TARGET_TOKENS
from badger_utils.ethplorer_utils import get_top_token_holders
from badger_utils.token_utils.utils import distribute_test_ether
from badger_utils.utils import is_address_eoa


class TokenWhaleNotFound(Exception):
    pass


def distribute_from_whale_realtime(
        recipient: Account,
        percentage: Optional[float] = 0.2,
        token_address: Optional[str] = TARGET_TOKENS[0]) -> None:
    token_whales = get_top_token_holders(token_address)['holders']
    target_whale = ''
    for token_whale in token_whales:
        # Use first whale that is not a contract
        if is_address_eoa(web3.toChecksumAddress(token_whale['address'])):
            target_whale = token_whale['address']  # type: str
            break
    if not target_whale:
        raise TokenWhaleNotFound(f"Cannot find whale for token {token_address}")
    if recipient.balance() < 2 * 10 ** 18:
        distribute_test_ether(recipient, Wei("5 ether"))
    force_ether = ForceEther.deploy({"from": recipient})
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
        percentage: Optional[float] = 0.8,
        tokens: Optional[List[str]] = None) -> None:
    """
    NOTE: This only works on Ethereum, since Ethplorer doesn't support any other chain
    """
    if not tokens:
        tokens = TARGET_TOKENS
    # Normal Transfers
    for token_addr in tokens:
        distribute_from_whale_realtime(recipient, percentage=percentage, token_address=token_addr)
        # This is needed because Ethplrorer API will raise exc if requests are made too often
        # for the free API key
        sleep(0.5)
