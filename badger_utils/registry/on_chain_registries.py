from brownie import BadgerRegistry  # noqa

from badger_utils.constants import ARBITRUM_NETWORK
from badger_utils.constants import BADGER_REGISTRY_ADDRESS
from badger_utils.constants import ETHEREUM_NETWORK
from badger_utils.constants import POLYGON_NETWORK
from badger_utils.network_manager import network_manager
from badger_utils.registry.chain_registry import ChainRegistry


class OnChainContractRegistries:
    """
    Contract registry for each chain pulled from on-chain
    """
    def __init__(self):
        self.registries = {}

    def initialize(self):
        # Badger registry has same address in all networks
        if not self.registries:
            for network in [ETHEREUM_NETWORK, POLYGON_NETWORK, ARBITRUM_NETWORK]:
                self.registries[network] = BadgerRegistry.at(BADGER_REGISTRY_ADDRESS)

    def get_registry(self, chain: str) -> BadgerRegistry:
        return self.registries[chain]

    def has_registry(self, chain: str) -> bool:
        return chain in self.registries.keys()

    def get_active_chain_registry(self) -> ChainRegistry:
        network_id = network_manager.get_active_network()
        return self.get_registry(network_id)


chain_registries = OnChainContractRegistries()
