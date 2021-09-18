import os

from dotmap import DotMap
import json


os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "dependency-artifacts/aragon",
    "Agent.json",
)
with open(os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "dependency-artifacts/aragon",
    "Agent.json",
)) as f:
    Agent = json.load(f)

with open(os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "dependency-artifacts/aragon",
    "Vault.json",
)) as f:
    Vault = json.load(f)

with open(os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "dependency-artifacts/aragon",
    "Voting.json",
)) as f:
    Voting = json.load(f)

with open(os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "dependency-artifacts/aragon",
    "Finance.json",
)) as f:
    Finance = json.load(f)


with open(os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "dependency-artifacts/aragon",
    "TokenManager.json",
)) as f:
    TokenManager = json.load(f)

with open(os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "dependency-artifacts/aragon",
    "CompanyTemplate.json",
)) as f:
    CompanyTemplate = json.load(f)

with open(os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "dependency-artifacts/aragon",
    "MiniMeToken.json",
)) as f:
    MiniMeToken = json.load(f)

with open(os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "dependency-artifacts/gnosis-safe",
    "MasterCopy.json",
)) as f:
    MasterCopy = json.load(f)

with open(os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "dependency-artifacts/gnosis-safe",
    "ProxyFactory.json",
)) as f:
    ProxyFactory = json.load(f)

with open(os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "dependency-artifacts/gnosis-safe",
    "GnosisSafe.json",
)) as f:
    GnosisSafe = json.load(f)

with open(os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "dependency-artifacts/open-zeppelin",
    "TokenTimelock.json",
)) as f:
    TokenTimelock = json.load(f)

with open(os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "dependency-artifacts/open-zeppelin-upgrades",
    "ProxyAdmin.json",
)) as f:
    ProxyAdmin = json.load(f)

with open(os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "dependency-artifacts/multicall",
    "Multicall.json",
)) as f:
    Multicall = json.load(f)

with open(os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "dependency-artifacts/digg/Mock.json",
)) as f:
    Mock = json.load(f)

with open(os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "dependency-artifacts/open-zeppelin-upgrades",
    "AdminUpgradeabilityProxy.json",
)) as f:
    AdminUpgradeabilityProxy = json.load(f)

with open(os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "dependency-artifacts/uniswap",
    "UniswapV2Pair.json",
)) as f:
    UniswapV2Pair = json.load(f)

with open(os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "dependency-artifacts/uniswap",
    "UniswapV2Factory.json",
)) as f:
    UniswapV2Factory = json.load(f)

with open(os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "dependency-artifacts/uniswap",
    "UniswapV2Router02.json",
)) as f:
    UniswapV2Router = json.load(f)

with open(os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "dependency-artifacts/wbtc",
    "wbtc.json",
)) as f:
    wbtc = json.load(f)

artifacts = DotMap(
    aragon=DotMap(
        Agent=Agent,
        CompanyTemplate=CompanyTemplate,
        Vault=Vault,
        Voting=Voting,
        Finance=Finance,
        TokenManager=TokenManager,
        MiniMeToken=MiniMeToken,
    ),
    gnosis_safe=DotMap(
        MasterCopy=MasterCopy, ProxyFactory=ProxyFactory, GnosisSafe=GnosisSafe
    ),
    digg=DotMap(
        Mock=Mock,
    ),
    open_zeppelin=DotMap(
        ProxyAdmin=ProxyAdmin,
        AdminUpgradeabilityProxy=AdminUpgradeabilityProxy,
        TokenTimelock=TokenTimelock,
    ),
    uniswap=DotMap(
        UniswapV2Factory=UniswapV2Factory,
        UniswapV2Router=UniswapV2Router,
        UniswapV2Pair=UniswapV2Pair,
    ),
    multicall=DotMap(multicall={"abi": Multicall}),
    wbtc=DotMap(wbtc={"abi": wbtc}),
)
