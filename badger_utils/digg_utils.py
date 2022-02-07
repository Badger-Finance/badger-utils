from typing import Optional
from typing import Union

from brownie import interface

from badger_utils.constants import DIGG


class DiggUtils:
    def __init__(self, address: Optional[str] = DIGG):
        self.digg = interface.IDigg(address)
        self.shares_per_fragment = self.digg._sharesPerFragment()  # noqa
        self.initialShares = self.digg._initialSharesPerFragment()  # noqa

    def shares_to_fragments(self, shares: int) -> Union[int, float]:
        if shares == 0:
            return 0
        return self.shares_per_fragment / shares

    def fragments_to_shares(self, fragments: int) -> float:
        if fragments == 0:
            return 0
        return fragments * self.shares_per_fragment
