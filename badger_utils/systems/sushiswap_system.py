from typing import Tuple

from brownie import accounts
from brownie import chain
from brownie import interface
from brownie import web3

from badger_utils.constants import MaxUint256


class SushiswapSystem:
    def __init__(self):
        from badger_utils.registry import registry
        self.contract_registry = registry.sushiswap
        self.factory = interface.IUniswapV2Factory(
            web3.toChecksumAddress(self.contract_registry.factory)
        )
        self.router = interface.IUniswapRouterV2(
            web3.toChecksumAddress(self.contract_registry.router)
        )
        self.chef = interface.ISushiChef(self.contract_registry.sushiChef)
        self.bar = interface.IxSushi(self.contract_registry.xsushiToken)

    def add_max_liquidity(self, token_a, token_b, signer):
        token_a = interface.IERC20(token_a)
        token_b = interface.IERC20(token_b)

        balance_a = token_a.balanceOf(signer) // 2
        balance_b = token_b.balanceOf(signer) // 2

        assert balance_a > 0
        assert balance_b > 0

        token_a.approve(self.router, MaxUint256, {"from": signer})
        token_b.approve(self.router, MaxUint256, {"from": signer})

        return self.router.addLiquidity(
            token_a.address,
            token_b.address,
            balance_a,
            balance_b,
            0,
            0,
            signer,
            chain.time() + 1000,
            {"from": signer},
        )

    def add_chef_rewards(self, pool):
        chef = self.chef

        owner = accounts.at(self.chef.owner(), force=True)
        # Make an average allocation of lp tokens.
        avg_alloc_point = chef.totalAllocPoint() / chef.poolLength()

        # Add staking pool (for rewards) if not exists or set the current allocation
        # to be receive average allocation points.
        pid, exists = self._get_pool(pool)
        if exists:
            chef.set(avg_alloc_point, pool, True, {"from": owner})
        else:
            # NB: If the lp token is added more than once, rewards will get messed up.
            chef.add(avg_alloc_point, pool, True, {"from": owner})

        pid = chef.poolLength() - 1
        chain.mine()

        chef.updatePool(pid, {"from": owner})
        chain.mine()

        return pid

    def _get_pool(self, pool) -> Tuple[int, bool]:
        chef = self.chef
        # Iterate over pools and look for pool first
        # NB: THIS IS EXPENSIVE AND SHOULD ONLY BE USED FOR TESTING.
        for pid in range(0, chef.poolLength()):
            (address, _, _, _) = chef.poolInfo(pid)
            if address == pool.address:
                return pid, True
        return -1, False
