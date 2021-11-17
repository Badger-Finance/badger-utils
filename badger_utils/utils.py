from typing import Optional

from brownie import interface
from brownie import web3


def approx(actual: int, expected: int, percentage_threshold: int) -> bool:
    diff = int(abs(actual - expected))
    if diff == 0:
        return True
    return diff < (actual * percentage_threshold // 100)


def val(amount=0, decimals=18, token: Optional[str] = None):
    # If no token specified, use decimals
    if token:
        decimals = interface.IERC20(token).decimals()

    return "{:,.18f}".format(amount / 10 ** decimals)


def is_address_eoa(address: str) -> bool:
    # If address is a contract, `get_code` will return hashed contract bytecode,
    # otherwise - empty bytestring
    return web3.eth.get_code(address) == b''
