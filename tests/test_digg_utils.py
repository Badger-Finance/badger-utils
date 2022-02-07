from brownie import accounts

from badger_utils.digg_utils import DiggUtils
from badger_utils.registry import artifacts
from brownie.network import web3
from brownie.network.contract import Contract


def test_digg_utils():
    abi = artifacts.digg["Mock"]["abi"]
    bytecode = artifacts.digg["Mock"]["bytecode"]
    mock = web3.eth.contract(abi=abi, bytecode=bytecode)
    deploy_txn = mock.constructor().buildTransaction()
    transaction = accounts[0].transfer(data=deploy_txn["data"])
    mock_contract = Contract.from_abi(
        "ProxyAdmin",
        web3.toChecksumAddress(transaction.contract_address),
        abi,
    )
    digg = DiggUtils(mock_contract.address)
    assert digg.shares_to_fragments(10) == 0
    assert digg.fragments_to_shares(10) == 0
