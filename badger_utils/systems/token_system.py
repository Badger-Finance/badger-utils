from brownie import interface


class TokenSystem:
    def __init__(self, registry):
        self.registry = registry

    def erc20_by_key(self, key):
        if key not in self.registry.tokens:
            raise Exception(f"Token with key {key} not found in registry")

        address = self.registry.tokens[key]
        return self.erc20_by_address(address)

    def erc20_by_address(self, address):
        return interface.IERC20(address)
