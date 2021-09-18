from typing import List

from brownie.network import web3
from brownie.network.account import Account
from brownie.network.contract import Contract
from brownie.network.gas.strategies import GasNowStrategy

from badger_utils.registry.artifacts import artifacts

gas_strategy = GasNowStrategy("rapid")


def deploy_proxy_admin(deployer: Account) -> Contract:
    abi = artifacts.open_zeppelin["ProxyAdmin"]["abi"]
    bytecode = artifacts.open_zeppelin["ProxyAdmin"]["bytecode"]

    proxy_admin = web3.eth.contract(abi=abi, bytecode=bytecode)

    deploy_txn = proxy_admin.constructor().buildTransaction()
    transaction = deployer.transfer(data=deploy_txn["data"])

    return Contract.from_abi(
        "ProxyAdmin",
        web3.toChecksumAddress(transaction.contract_address),
        abi,
    )


def deploy_proxy_uninitialized(
    contract_name: str, logic_abi: List, logic: str, proxy_admin: str, deployer: Account
) -> Contract:
    abi = artifacts.open_zeppelin["AdminUpgradeabilityProxy"]["abi"]
    bytecode = artifacts.open_zeppelin["AdminUpgradeabilityProxy"]["bytecode"]

    admin_upgradeability_proxy = web3.eth.contract(abi=abi, bytecode=bytecode)

    deploy_txn = admin_upgradeability_proxy.constructor(
        logic, proxy_admin, web3.toBytes(hexstr="0x")
    ).buildTransaction()

    transaction = deployer.transfer(data=deploy_txn["data"])

    return Contract.from_abi(contract_name, transaction.contract_address, logic_abi)


def deploy_proxy(
    contract_name: str, logic_abi: List, logic: str,
    proxy_admin: str, initializer: str, deployer: Account
):
    abi = artifacts.open_zeppelin["AdminUpgradeabilityProxy"]["abi"]
    bytecode = artifacts.open_zeppelin["AdminUpgradeabilityProxy"]["bytecode"]

    admin_upgradeability_proxy = web3.eth.contract(abi=abi, bytecode=bytecode)

    deploy_txn = admin_upgradeability_proxy.constructor(
        logic, proxy_admin, web3.toBytes(hexstr=initializer)
    ).buildTransaction()

    transaction = deployer.transfer(data=deploy_txn["data"])

    return Contract.from_abi(contract_name, transaction.contract_address, logic_abi)
