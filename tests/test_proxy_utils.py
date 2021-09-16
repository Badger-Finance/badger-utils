import pytest
from brownie import accounts

from utils.proxy_utils import deploy_proxy_admin


def test_deploy_proxy_admin_deployed():
    contract = deploy_proxy_admin(accounts[0])
    assert contract.address is not None
    assert accounts[0].gas_used != 0
    assert contract.owner() == accounts[0].address


def test_deploy_proxy_admin__not_enough_balance():
    accounts[9].transfer(accounts[1], "100 ether", gas_price=0)

    with pytest.raises(ValueError):
        deploy_proxy_admin(accounts[9])
