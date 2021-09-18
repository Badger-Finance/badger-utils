import pytest
from brownie import accounts

from badger_utils.proxy_utils import deploy_proxy
from badger_utils.proxy_utils import deploy_proxy_admin
from badger_utils.proxy_utils import deploy_proxy_uninitialized
from badger_utils.registry.artifacts import artifacts


@pytest.fixture(scope='module', autouse=True)
def burn_account_balance():
    accounts[9].transfer(accounts[1], "100 ether", gas_price=0)


def test_deploy_proxy_admin_deployed():
    contract = deploy_proxy_admin(accounts[0])
    assert contract.address is not None
    assert accounts[0].gas_used != 0
    assert contract.owner() == accounts[0].address


def test_deploy_proxy_admin__not_enough_balance():
    with pytest.raises(ValueError):
        deploy_proxy_admin(accounts[9])


def test_deploy_proxy_unitialized():
    proxy_admin_contract = deploy_proxy_admin(accounts[1])
    contract = deploy_proxy_uninitialized(
        "TokenTimelock",
        logic_abi=artifacts.open_zeppelin["TokenTimelock"]["abi"],
        logic=proxy_admin_contract.address,
        proxy_admin=proxy_admin_contract.address,
        deployer=accounts[1],
    )
    assert contract.address is not None
    assert accounts[1].gas_used != 0


def test_deploy_proxy():
    proxy_admin_contract = deploy_proxy_admin(accounts[1])
    contract = deploy_proxy(
        "TokenTimelock",
        logic_abi=artifacts.open_zeppelin["TokenTimelock"]["abi"],
        logic=proxy_admin_contract.address,
        proxy_admin=proxy_admin_contract.address,
        initializer="0x",
        deployer=accounts[1],
    )
    assert contract.address is not None
    assert accounts[1].gas_used != 0
