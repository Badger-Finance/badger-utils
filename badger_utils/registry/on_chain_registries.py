from badger_utils.constants import ARBITRUM_NETWORK
from badger_utils.constants import BADGER_REGISTRY_ADDRESS
from badger_utils.constants import ETHEREUM_NETWORK
from badger_utils.constants import DEVELOPMENT_NETWORK
from badger_utils.constants import POLYGON_NETWORK
from badger_utils.registry.base_registry import BaseRegistry


class OnChainContractRegistries(BaseRegistry):
    """
    Contract registry for each chain pulled from on-chain
    """

    def initialize(self):
        """
        Call this method to map BadgerRegistry contract to on-chain implementation
        """
        try:
            from brownie import BadgerRegistry  # noqa
        except ImportError:
            return
        # Badger registry has same address in all networks
        if not self.registries:
            for network in [ETHEREUM_NETWORK, POLYGON_NETWORK,
                            ARBITRUM_NETWORK, DEVELOPMENT_NETWORK]:
                self.registries[network] = BadgerRegistry.at(BADGER_REGISTRY_ADDRESS)


chain_registries = OnChainContractRegistries()
