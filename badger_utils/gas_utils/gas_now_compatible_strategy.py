import requests
from brownie.network.gas.bases import SimpleGasStrategy


GASNOW_COMPATIBLE_API = "https://etherchain.org/api/gasnow"


# This module is a port for GasNowStrategy strategy. As GasNow service is closed, use
# gasnow org API which is a Gasnow API compatible enpoint
class GasNowCompatibleStrategy(SimpleGasStrategy):
    def __init__(self, speed: str = "fast"):
        if speed not in ("rapid", "fast", "standard", "slow"):
            raise ValueError("`speed` must be one of: rapid, fast, standard, slow")
        self.speed = speed

    def get_gas_price(self) -> int:
        response = requests.get(GASNOW_COMPATIBLE_API)
        response.raise_for_status()
        return response.json()["data"][self.speed]
