from brownie.network import web3
from brownie.network.contract import Contract
from brownie.network.account import Account
from brownie.network.gas.strategies import GasNowStrategy

from utils.registry.artifacts import artifacts

gas_strategy = GasNowStrategy("rapid")


def deploy_proxy_admin(deployer: Account):
    abi = artifacts.open_zeppelin["ProxyAdmin"]["abi"]
    bytecode = artifacts.open_zeppelin["ProxyAdmin"]["bytecode"]

    proxy_admin = web3.eth.contract(abi=abi, bytecode=bytecode)

    deploy_txn = proxy_admin.constructor().buildTransaction()
    tx = deployer.transfer(data=deploy_txn["data"])

    return Contract.from_abi(
        "ProxyAdmin",
        web3.toChecksumAddress(tx.contract_address),
        abi,
    )


def deploy_proxy_uninitialized(
    contract_name: str, logic_abi, logic: str, proxy_admin, deployer: Account
):
    abi = artifacts.open_zeppelin["AdminUpgradeabilityProxy"]["abi"]
    bytecode = artifacts.open_zeppelin["AdminUpgradeabilityProxy"]["bytecode"]

    admin_upgradeability_proxy = web3.eth.contract(abi=abi, bytecode=bytecode)

    deploy_txn = admin_upgradeability_proxy.constructor(
        logic, proxy_admin, web3.toBytes(hexstr="0x")
    ).buildTransaction()

    tx = deployer.transfer(data=deploy_txn["data"])

    return Contract.from_abi(contract_name, tx.contract_address, logic_abi)


def deploy_proxy(
    contract_name, logic_abi, logic, proxy_admin, initializer, deployer: Account
):
    abi = artifacts.open_zeppelin["AdminUpgradeabilityProxy"]["abi"]
    bytecode = artifacts.open_zeppelin["AdminUpgradeabilityProxy"]["bytecode"]

    admin_upgradeability_proxy = web3.eth.contract(abi=abi, bytecode=bytecode)

    deploy_txn = admin_upgradeability_proxy.constructor(
        logic, proxy_admin, web3.toBytes(hexstr=initializer)
    ).buildTransaction()

    tx = deployer.transfer(data=deploy_txn["data"])

    print("Deploying contract:", contract_name, "address:", tx.contract_address)
    return Contract.from_abi(contract_name, tx.contract_address, logic_abi)
