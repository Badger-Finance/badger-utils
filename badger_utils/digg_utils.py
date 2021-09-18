from typing import Optional
from typing import Union

from brownie import interface

from badger_utils.constants import DIGG


class DiggUtils:
    def __init__(self, address: Optional[str] = DIGG):
        self.digg = interface.IDigg(address)
        self.sharesPerFragment = self.digg._sharesPerFragment()
        self.initialShares = self.digg._initialSharesPerFragment()

    def shares_to_fragments(self, shares: int) -> Union[int, float]:
        if shares == 0:
            return 0
        return self.sharesPerFragment / shares
