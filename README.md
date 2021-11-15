# badger-utils library

This is the library for all badger utils that were moved from [badger-system](https://github.com/Badger-Finance/badger-system) repo.

| Build  | Coverage | PYPI | 
| ------------- | ------------- | ------------- |
| [![Tests](https://github.com/SHAKOTN/badger-utils/actions/workflows/main.yml/badge.svg?branch=master)](https://github.com/SHAKOTN/badger-utils/actions/workflows/main.yml) | [![codecov](https://codecov.io/gh/Badger-Finance/badger-utils/branch/master/graph/badge.svg?token=210VN0EJ90)](https://codecov.io/gh/Badger-Finance/badger-utils)  | [![PyPI version](https://badge.fury.io/py/badger-utils.svg)](https://badge.fury.io/py/badger-utils) |

---

## Requirements
To make use of library you would need some interfaces and contracts to be [compiled](https://eth-brownie.readthedocs.io/en/stable/compile.html) 
and injected by brownie into your brownie project.
List of required interfaces can be found [here](https://github.com/SHAKOTN/badger-utils/tree/master/interfaces)

You also need some contracts to be compiled as well:
```
ForceEther, SafeMath, Token, BadgerRegistry
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
- [Coingecko Utils](#using-coingecko-utils)
- [Gas utils module](#using-gas_utils-module)
- [Network utils](#using-network-utils)
- [Proxy utils](#using-proxy-utils)
- [Distribute from whales realtime](#using-distribute-from-whales-realtime)
- [Token utils](#using-token-utils)
- [Constants](#using-constants)
- [Tx timer](#using-tx-timer)
- [Artifacts](#using-artifacts)
- [Local registry](#locally-defined-registry)
- [On chain registry](#on-chain-registry)
- [Systems](#using-systems)

Giving some examples on library usage:
### Using coingecko utils
```python
from badger_utils.coingecko_utils import fetch_usd_price
some_erc_token = interface.IERC20(Token)
usd_price = fetch_usd_price(some_erc_token.address)
```

### Using gas_utils module
```python
from badger_utils.gas_utils import GasStrategies

# Class initialization will initialize everything and fetch gas prices
strategies = GasStrategies()

price = strategies.optimal_price()
# check gas cost:
strategies.gas_cost(gas_estimate=21000)
# Set default strategy:
strategies.set_default_for_active_chain()
```
**NOTE:** If you want to use Anyblock historical data in gas analysis, consider adding auth keys
from anyblock account:
```shell
export ANYBLOCK_EMAIL=email@gmail.com
export ANYBLOCK_KEY=<YOU ANYBLOCK API KEY>
```
otherwise `def analyze_gas` function will always return static data:
```python
DotMap(mode=999999999999999999, median=999999999999999999, std=999999999999999999)
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

### Using distribute from whales realtime
If you want to use some other Ethplorer key to fetch whales, set env variable: ETHPLORER_API_KEY
```shell
export ETHPLORER_API_KEY=<API_KEY>
```
Otherwise, ethplorer key will be used by default, which is a bit slow
```python
import token  # some deployed token
from brownie import accounts
from badger_utils.token_utils.distribute_from_whales_realtime import distribute_from_whales_realtime

token.transfer(
    "0x19d099670a21bC0a8211a89B84cEdF59AbB4377F", 100000, {'from': accounts[0]}
)
distribute_from_whales_realtime(accounts[1], percentage=0.8)
```

### Using token utils
**LEGACY**. Consider using `distribute_from_whales_realtime` module
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

### On chain registry
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
