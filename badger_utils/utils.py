from typing import Optional

from brownie import interface


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
