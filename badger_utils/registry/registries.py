from brownie import BadgerRegistry  # noqa

from badger_utils.registry.base_registry import BaseRegistry
from badger_utils.registry.bsc_registry import bsc_registry
from badger_utils.registry.eth_registry import eth_registry


class ContractRegistries(BaseRegistry):
    """
    Contract registry for each chain
    """

    def __init__(self):
        super().__init__()
        self.registries["eth"] = eth_registry
        self.registries["development"] = eth_registry
        self.registries["bsc"] = bsc_registry


registries = ContractRegistries()
registry = registries.get_active_chain_registry()
