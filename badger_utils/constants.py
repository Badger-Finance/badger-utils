from enum import Enum

from brownie import Wei
from brownie.network import web3

AddressZero = "0x0000000000000000000000000000000000000000"
MaxUint256 = str(int(2 ** 256 - 1))
EmptyBytes32 = "0x0000000000000000000000000000000000000000000000000000000000000000"

DEFAULT_ADMIN_ROLE = (
    "0x0000000000000000000000000000000000000000000000000000000000000000"
)

TOKEN_LOCKER_ROLE = web3.keccak(text="TOKEN_LOCKER_ROLE").hex()
ROOT_UPDATER_ROLE = web3.keccak(text="ROOT_UPDATER_ROLE").hex()
GUARDIAN_ROLE = web3.keccak(text="GUARDIAN_ROLE").hex()
APPROVED_STAKER_ROLE = web3.keccak(text="APPROVED_STAKER_ROLE").hex()
PAUSER_ROLE = web3.keccak(text="PAUSER_ROLE").hex()
UNPAUSER_ROLE = web3.keccak(text="UNPAUSER_ROLE").hex()
DISTRIBUTOR_ROLE = web3.keccak(text="DISTRIBUTOR_ROLE").hex()
ROOT_PROPOSER_ROLE = web3.keccak(text="ROOT_PROPOSER_ROLE").hex()
ROOT_VALIDATOR_ROLE = web3.keccak(text="ROOT_VALIDATOR_ROLE").hex()
APPROVED_ACCOUNT_ROLE = web3.keccak(text="APPROVED_ACCOUNT_ROLE").hex()

DIGG = "0x798D1bE841a82a273720CE31c822C61a67a601C3"
BADGER = "0x3472A5A71965499acd81997a54BBA8D852C6E53d"
BBADGER = "0x19d97d8fa813ee2f51ad4b4e04ea08baf4dffc28"
SPELL = "0x090185f2135308bad17527004364ebcc2d37e5f6"
FARM = "0xa0246c9032bC3A600820415aE600c6388619A14D"
XSUSHI = "0x8798249c2E607446EfB7Ad49eC89dD1865Ff4272"
DFD = "0x20c36f062a31865bED8a5B1e512D9a1A20AA333A"
BCVXCRV = "0x2B5455aac8d64C14786c3a29858E43b5945819C0"
BCVX = "0x53C8E199eb2Cb7c01543C137078a038937a68E40"
PNT = "0x89Ab32156e46F46D02ade3FEcbe5Fc4243B9AAeD"
BOR = "0x3c9d6c1C73b31c837832c72E04D3152f051fc1A9"

TOKENS_TO_CHECK = {
    "Badger": BADGER,
    "Digg": DIGG,
    "Farm": FARM,
    "xSushi": XSUSHI,
    "Dfd": DFD,
    "bCvxCrv": BCVXCRV,
    "bCvx": BCVX,
    "Pnt": PNT,
    "Bor": BOR,
}

BADGER_TREE = "0x660802Fc641b154aBA66a62137e71f331B6d787A"

PEAK_ADDRESSES = [
    "0x825218beD8BE0B30be39475755AceE0250C50627",
    "0x41671BA1abcbA387b9b2B752c205e22e916BE6e3",
]

MAX_BOOST = 3
DIGG_SETTS = ["native.uniDiggWbtc", "native.sushiDiggWbtc", "native.digg"]
BADGER_SETTS = ["native.badger", "native.uniBadgerWbtc", "native.sushiBadgerWbtc"]
NATIVE_DIGG_SETTS = ["native.uniDiggWbtc", "native.sushiDiggWbtc"]

NON_NATIVE_SETTS = [
    "native.renCrv",
    "native.sbtcCrv",
    "native.tbtcCrv",
    "native.sushiWbtcEth",
    "harvest.renCrv",
    "yearn.wbtc",
    "experimental.sushiIBbtcWbtc",
    "native.hbtcCrv",
    "native.pbtcCrv",
    "native.obtcCrv",
    "native.bbtcCrv",
    "native.tricrypto",
    "native.cvxCrv",
    "native.cvx",
]

NO_GEYSERS = [
    "native.digg",
    "experimental.sushiIBbtcWbtc",
    "experimental.digg",
    "native.hbtcCrv",
    "native.pbtcCrv",
    "native.obtcCrv",
    "native.bbtcCrv",
    "native.tricrypto",
    "native.cvxCrv",
    "native.cvx",
]

SETT_BOOST_RATIOS = {
    "native.uniDiggWbtc": 0.5,
    "native.sushiDiggWbtc": 0.5,
    "native.uniBadgerWbtc": 0.5,
    "native.sushiBadgerWbtc": 0.5,
    "native.badger": 1,
    "native.digg": 1,
    "native.renCrv": 1,
    "native.sbtcCrv": 1,
    "native.tbtcCrv": 1,
    "harvest.renCrv": 1,
    "native.sushiWbtcEth": 1,
    "yearn.wbtc": 1,
    "experimental.sushiIBbtcWbtc": 1,
    "native.hbtcCrv": 1,
    "native.pbtcCrv": 1,
    "native.obtcCrv": 1,
    "native.bbtcCrv": 1,
    "native.tricrypto": 1,
    "native.cvxCrv": 0.1,
    "native.cvx": 0.1,
}

CONVEX_SETTS = ["native.hbtcCrv", "native.pbtcCrv", "native.obtcCrv", "native.bbtcCrv"]


class WhaleRegistryAction(Enum):
    DISTRIBUTE_FROM_EOA = (0,)
    DISTRIBUTE_FROM_CONTRACT = (1,)
    POPULATE_NEW_SUSHI_LP = 2


class ContractSystems(Enum):
    ARAGON = ("aragon",)
    GNOSIS_SAFE = ("gnosis-safe",)
    OPEN_ZEPPELIN = ("open-zeppelin",)
    UNISWAP = ("uniswap",)
    SUSHISWAP = ("sushiswap",)
    MULTICALL = ("multicall",)
    PICKLE = ("pickle",)
    HARVEST = ("harvest",)
    CURVE = ("curve",)
    CHAINLINK = ("chainlink",)
    TOKENS = "tokens"


BADGER_REGISTRY_ADDRESS = "0xFda7eB6f8b7a9e9fCFd348042ae675d1d652454f"  # Multichain BadgerRegistry

ETHEREUM_NETWORK = "eth"
BINANCE_NETWORK = "bsc"
POLYGON_NETWORK = "polygon"
ARBITRUM_NETWORK = "arbitrum"
DEVELOPMENT_NETWORK = "development"

SUPPORTED_NETWORKS = [ETHEREUM_NETWORK, BINANCE_NETWORK, POLYGON_NETWORK, ARBITRUM_NETWORK]


EXPONENTIAL_SCALING_CONFIG = {
    "initial_gas_price": "100 gwei",
    "max_gas_price": "1000 gwei",
}

BSC_STATIC_PRICE = Wei("10 gwei")
HISTORICAL_MAINNET_ELASTIC_URL = "https://api.anyblock.tools/ethereum/ethereum/mainnet/es/"

NUMBER_OF_BINS = 60  # number of bins for histogram

TARGET_TOKENS = [
    "0x3472A5A71965499acd81997a54BBA8D852C6E53d",
    "0x19D97D8fA813EE2f51aD4B4e04EA08bAf4DFfC28",
    "0xAf5A1DECfa95BAF63E0084a35c62592B774A2A87",
    "0xcD7989894bc033581532D2cd88Da5db0A4b12859",
    "0xe86204c4eddd2f70ee00ead6805f917671f56c52",
    "0x075b1bb99792c9E1041bA13afEf80C91a1e70fB3",
    "0xd04c48A53c111300aD41190D63681ed3dAd998eC",
    "0x49849C98ae39Fff122806C06791Fa73784FB3675",
    "0x6dEf55d2e18486B9dDfaA075bc4e4EE0B28c1545",
    "0x64eda51d3Ad40D56b9dFc5554E06F94e1Dd786Fd",
    "0xb9D076fDe463dbc9f915E5392F807315Bf940334",
    "0xb19059ebb43466C323583928285a49f558E572Fd",
    "0xDE5331AC4B3630f94853Ff322B66407e0D6331E8",
    "0x2fE94ea3d5d4a175184081439753DE15AeF9d614",
    "0x410e3E86ef427e30B9235497143881f717d93c2A",
    "0x2260FAC5E5542a773Aa44fBCfeDf7C193bc2C599",
    "0x110492b31c59716AC47337E616804E3E3AdC0b4a",
    "0xCEfF51756c56CeFFCA006cD410B03FFC46dd3a58",
    "0x758A43EE2BFf8230eeb784879CdcFF4828F2544D",
    "0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48",
    "0x798D1bE841a82a273720CE31c822C61a67a601C3",
    "0xeb4c2781e4eba804ce9a9803c67d0893436bb27d",
    "0xcA3d75aC011BF5aD07a98d02f18225F9bD9A6BDF",
    "0x4e3fbd56cd56c3e72c1403e103b45db9da5b9d2b",
    "0x62b9c7356a2dc64a1969e19c23e4f579f9810aa7",
    "0xFbdCA68601f835b27790D98bbb8eC7f05FDEaA9B",
]
