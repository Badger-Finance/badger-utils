from badger_utils.network_manager import network_manager
from badger_utils.registry.chain_registry import ChainRegistry


class BaseRegistry:
    def __init__(self):
        self.registries = {}

    def get_registry(self, chain: str):
        return self.registries[chain]

    def has_registry(self, chain: str) -> bool:
        return chain in self.registries.keys()

    def get_active_chain_registry(self) -> ChainRegistry:
        network_id = network_manager.get_active_network()
        return self.get_registry(network_id)
