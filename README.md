# badger-utils library

This is the library for all badger utils that were moved from [badger-system](https://github.com/Badger-Finance/badger-system) repo.

| Build  | Coverage |
| ------------- | ------------- |
| [![Tests](https://github.com/SHAKOTN/badger-utils/actions/workflows/main.yml/badge.svg?branch=master)](https://github.com/SHAKOTN/badger-utils/actions/workflows/main.yml) | [![codecov](https://codecov.io/gh/SHAKOTN/badger-utils/branch/master/graph/badge.svg?token=210VN0EJ90)](https://codecov.io/gh/SHAKOTN/badger-utils)  |

---

## Features and Utils
**Current state** of library and components and what was moved from [badger-system repo](https://github.com/Badger-Finance/badger-system):
### Systems:
1. AaveSystem
2. SushiSwapSystem
3. CompoundSystem

### Utils:
1. Registry
2. Proxy utils
3. Coingecko utils
4. Network manager
5. Time utils
6. Token utils
7. Digg utils
8. txTimer utility
9. Full constants module
10. Different misc functions

### Testing Tools:
`distribute_from_whales` and some other balance calculation functions

## Requirements
To make use of library you would need some interfaces and contracts to be [compiled](https://eth-brownie.readthedocs.io/en/stable/compile.html) 
and injected by brownie into your brownie project.
List of required interfaces:
```
BadgerGuestListAPI
GuestListAPI
ICToken
IChainlinkForwarder
IComptroller
IDigg
IDiggDistributor
IDiggRewardsFaucet
IDiggStrategy
IERC20
IERC20Detailed
ILendingPool
IMedianOracle
IStakingRewards
ISushiChef
IUniswapExchange
IUniswapFactory
IUniswapPair
IUniswapRouterV2
IUniswapV2Factory
IUniswapV2Pair
IWETH
IxSushi
RegistryAPI
StrategyAPI
USDT
WETH
```

You also need some contracts to be compiled as well:
```
ForceEther, SafeMath, Token
```

Please, not that it can all be copied from 

## Installing library
`pip install badger-utils`

## Using library

