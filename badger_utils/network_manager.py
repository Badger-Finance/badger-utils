import re
import sys
from typing import Optional

from brownie import network

from badger_utils.constants import ARBITRUM_NETWORK
from badger_utils.constants import DEVELOPMENT_NETWORK
from badger_utils.constants import BINANCE_NETWORK
from badger_utils.constants import ETHEREUM_NETWORK
from badger_utils.constants import POLYGON_NETWORK


class NetworkManager:
    @staticmethod
    def network_name(raw_network_name: str) -> Optional[str]:
        if re.match(r"^mainnet", raw_network_name):
            return ETHEREUM_NETWORK
        if re.match(r"(?:bsc|binance)", raw_network_name):
            return BINANCE_NETWORK
        if re.match(r"^polygon", raw_network_name):
            return POLYGON_NETWORK
        if re.match(r"^arbitrum", raw_network_name):
            return ARBITRUM_NETWORK
        if re.match(r"^development", raw_network_name):
            return DEVELOPMENT_NETWORK
        return None

    @staticmethod
    def get_active_network() -> str:
        active_network = network.show_active()

        if active_network is None:
            if "--network" not in sys.argv:
                name = "eth"
            else:
                network_idx = sys.argv.index("--network")
                name = NetworkManager.network_name(sys.argv[network_idx + 1])
        else:
            name = NetworkManager.network_name(active_network)

        if not name:
            raise Exception(f"Chain ID {active_network} not recognized")

        return name

    @staticmethod
    def get_active_network_badger_deploy() -> str:
        active_network = NetworkManager.get_active_network()
        if active_network == ETHEREUM_NETWORK:
            return "deploy-final.json"
        elif active_network == BINANCE_NETWORK:
            return "badger-deploy-bsc.json"
        else:
            raise Exception(f"No badger deploy file registered for network {active_network}")


network_manager = NetworkManager()
