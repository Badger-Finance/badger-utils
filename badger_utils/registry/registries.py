from badger_utils.network_manager import network_manager
from badger_utils.registry.bsc_registry import bsc_registry
from badger_utils.registry.chain_registry import ChainRegistry
from badger_utils.registry.eth_registry import eth_registry


class ContractRegistries:
    """
    Contract registry for each chain
    """

    def __init__(self):
        self.registries = {}
        self.registries["eth"] = eth_registry
        self.registries["bsc"] = bsc_registry

    def has_registry(self, chain: str):
        return chain in self.registries.keys()

    def get_registry(self, chain: str):
        return self.registries[chain]

    def get_active_chain_registry(self) -> ChainRegistry:
        network_id = network_manager.get_active_network()
        return self.get_registry(network_id)


registries = ContractRegistries()
registry = registries.get_active_chain_registry()
