import re
import sys
from typing import Optional

from brownie import network

ETHEREUM_NETWORK = "eth"
BINANCE_NETWORK = "bsc"


class NetworkManager:
    @staticmethod
    def network_name(raw_network_name: str) -> Optional[str]:
        if re.match(r"^mainnet", raw_network_name):
            return "eth"
        if re.match(r"(?:bsc|binance)", raw_network_name):
            return "bsc"
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
