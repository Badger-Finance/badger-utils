import requests
from brownie.network.gas.bases import SimpleGasStrategy


# This module is a port for GasNowStrategy strategy. As GasNow service is closed, use
# gasnow org API which is a Gasnow API compatible enpoint
class GasNowCompatibleStrategy(SimpleGasStrategy):
    def __init__(self, speed: str = "fast"):
        if speed not in ("rapid", "fast", "standard", "slow"):
            raise ValueError("`speed` must be one of: rapid, fast, standard, slow")
        self.speed = speed

    def get_gas_price(self) -> int:
        response = requests.get("https://www.gasnow.org/api/v3/gas/price")
        response.raise_for_status()
        return response.json()["data"][self.speed]
