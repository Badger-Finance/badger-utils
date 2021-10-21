# badger-utils library

This is the library for all badger utils that were moved from [badger-system](https://github.com/Badger-Finance/badger-system) repo.

| Build  | Coverage | PYPI | 
| ------------- | ------------- | ------------- |
| [![Tests](https://github.com/SHAKOTN/badger-utils/actions/workflows/main.yml/badge.svg?branch=master)](https://github.com/SHAKOTN/badger-utils/actions/workflows/main.yml) | [![codecov](https://codecov.io/gh/Badger-Finance/badger-utils/branch/master/graph/badge.svg?token=210VN0EJ90)](https://codecov.io/gh/Badger-Finance/badger-utils)  | [![PyPI version](https://badge.fury.io/py/badger-utils.svg)](https://badge.fury.io/py/badger-utils) |


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
List of required interfaces can be found [here](https://github.com/SHAKOTN/badger-utils/tree/master/interfaces)

You also need some contracts to be compiled as well:
```
ForceEther, SafeMath, Token
```

## Installing library
`pip install badger-utils`

## To run tests:
```
$ virtualenv venv
$ source venv/bin/activate
$ make
$ brownie test
```

## Using library
Giving some examples on library usage:
### Using coingecko utils:
```python
from badger_utils.coingecko_utils import fetch_usd_price
some_erc_token = interface.IERC20(Token)
usd_price = fetch_usd_price(some_erc_token.address)
```

### Using network utils
```python
from badger_utils.network_manager import network_manager
network = network_manager.get_active_network()
badger_deploy_file = network_manager.get_active_network_badger_deploy()
```

### Using proxy utils
```python
from badger_utils.proxy_utils import deploy_proxy_admin
from brownie import accounts

contract = deploy_proxy_admin(accounts[0])
assert contract.address is not None
```

### Using token utils
```python
import token  # some deployed token
from brownie import accounts
from badger_utils.token_utils import distribute_from_whales

token.transfer(
    "0x19d099670a21bC0a8211a89B84cEdF59AbB4377F", 100000, {'from': accounts[0]}
)
distribute_from_whales(accounts[1], percentage=0.8)
```

### Using constants
```python
from badger_utils.constants import AddressZero
from badger_utils.constants import TOKEN_LOCKER_ROLE
from badger_utils.constants import ContractSystems
```

### Using tx timer
```python
from badger_utils.tx_timer import tx_timer
from brownie import accounts

tx_timer.prepare_timer(accounts[0], "Harvest")
tx_timer.start_timer(accounts[0], 'Harvest')
tx_timer.end_timer()
```

### Using artifacts
```python
from badger_utils.registry.artifacts import artifacts

timelock_abi = artifacts.open_zeppelin["TokenTimelock"]["abi"]
```

### Using registries

### On chain registry:
```python
from badger_utils.registry import chain_registries

chain_registries.initialize()
chain_registries.get("badgerTree")
```
### Locally defined registry
**NOTE:** This is legacy way of working with registries
```python
from brownie import web3
from badger_utils.registry import registry

checksummed = web3.toChecksumAddress(registry.tokens.wbtc)
```

### Using systems
```python
from badger_utils.systems import SushiswapSystem
```
