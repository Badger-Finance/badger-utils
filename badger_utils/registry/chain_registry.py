from badger_utils.systems.aave_system import AaveSystem
from badger_utils.systems.compound_system import CompoundSystem
from badger_utils.systems.token_system import TokenSystem
from badger_utils.systems.yearn_system import YearnSystem


class ChainRegistry:
    def __init__(
        self,
        curve=None,
        convex=None,
        uniswap=None,
        open_zeppelin=None,
        aragon=None,
        sushiswap=None,
        sushi=None,
        gnosis_safe=None,
        onesplit=None,
        pickle=None,
        harvest=None,
        tokens=None,
        whales=None,
        multicall=None,
        multisend=None,
        pancake=None,
        badger=None,
        yearn=None,
        aave=None,
        compound=None,
        chainlink=None,
        defidollar=None,
        digg=None,
    ):
        self.curve = curve
        self.convex = convex
        self.uniswap = uniswap
        self.open_zeppelin = open_zeppelin
        self.aragon = aragon
        self.sushiswap = sushiswap
        self.sushi = sushi
        self.gnosis_safe = gnosis_safe
        self.onesplit = onesplit
        self.pickle = pickle
        self.harvest = harvest
        self.tokens = tokens
        self.whales = whales
        self.multicall = multicall
        self.multisend = multisend
        self.pancake = pancake
        self.badger = badger
        self.yearn = yearn
        self.aave = aave
        self.compound = compound
        self.defidollar = defidollar
        self.chainlink = chainlink

    def yearn_system(self) -> YearnSystem:
        if self.yearn is None:
            raise Exception("No yearn system registered")
        return YearnSystem(self)

    def token_system(self) -> TokenSystem:
        if self.tokens is None:
            raise Exception("No yearn system registered")
        return TokenSystem(self)

    def aave_system(self) -> AaveSystem:
        if self.aave is None:
            raise Exception("No aave system registered")
        return AaveSystem(self)

    def compound_system(self) -> CompoundSystem:
        if self.aave is None:
            raise Exception("No aave system registered")
        return CompoundSystem(self)
