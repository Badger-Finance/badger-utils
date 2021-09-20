from brownie.network.contract import Contract
from brownie.network.account import Account


class Balances:
    def __init__(self):
        self.balances = {}

    def set(self, token: Contract, account: Account, value: int):
        if token.address not in self.balances:
            self.balances[token.address] = {}
        self.balances[token.address][account.address] = value

    def get(self, token, account):
        return self.balances[token][account]
