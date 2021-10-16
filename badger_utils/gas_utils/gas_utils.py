from brownie import Wei
from brownie.network import gas_price
from brownie.network.gas.strategies import ExponentialScalingStrategy
from brownie.network.gas.strategies import GasNowStrategy
from brownie.network.gas.strategies import SimpleGasStrategy
from web3 import Web3

from badger_utils.constants import BSC_STATIC_PRICE
from badger_utils.constants import EXPONENTIAL_SCALING_CONFIG
from badger_utils.gas_utils.analyze_gas import analyze_gas
from badger_utils.network_manager import network_manager


class StaticGasStrategy(SimpleGasStrategy):
    def __init__(self, price) -> None:
        self.price = price
        super().__init__()

    def get_gas_price(self) -> int:
        return self.price


class GasStrategies:
    def __init__(self):
        self.standard = GasNowStrategy("standard")
        self.fast = GasNowStrategy("fast")
        self.rapid = GasNowStrategy("rapid")
        self.bsc_static = StaticGasStrategy(BSC_STATIC_PRICE)
        self.analyzed = analyze_gas({"timeframe": "minutes", "periods": 15})

        self.exponential_scaling = ExponentialScalingStrategy(
            initial_gas_price=self.standard.get_gas_price(),
            max_gas_price=Wei(EXPONENTIAL_SCALING_CONFIG["max_gas_price"]),
            time_duration=120,
        )

        self.exponential_scaling_fast = ExponentialScalingStrategy(
            initial_gas_price=self.fast.get_gas_price(),
            max_gas_price=Wei(EXPONENTIAL_SCALING_CONFIG["max_gas_price"]),
            time_duration=60,
        )

    def set_default(self, strategy):
        gas_price(strategy)

    def gas_cost(self, gas_estimate):
        """
        Total gas cost of estimate in wei
        """
        return Web3.toWei(
            Web3.fromWei(self.fast.get_gas_price(), "gwei") * gas_estimate, "gwei"
        )

    def set_default_for_active_chain(self):
        chain = network_manager.get_active_network()
        if chain == "eth":
            self.set_default(self.exponential_scaling)
        elif chain == "bsc":
            self.set_default(self.bsc_static)

    def optimal_price(self):
        return min(self.fast.get_gas_price(), self.analyzed.mode)


gas_strategies = GasStrategies()
