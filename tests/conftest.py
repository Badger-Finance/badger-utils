import pytest
from brownie import BadgerRegistry  # noqa
from brownie import accounts


@pytest.fixture(scope="function", autouse=True)
def isolate(fn_isolation):
    # perform a chain rewind after completing each test, to ensure proper isolation
    # https://eth-brownie.readthedocs.io/en/v1.10.3/tests-pytest-intro.html#isolation-fixtures
    pass


@pytest.fixture(scope="module")
def token(Token, accounts):
    return Token.deploy("Test Token", "TST", 18, 1e21, {'from': accounts[0]})


@pytest.fixture
def mock_target_tokens(token, mocker):
    mocker.patch(
        "badger_utils.token_utils.distribute_from_whales_realtime.TARGET_TOKENS",
        [token.address]
    )
    yield


@pytest.fixture(scope="module")
def badger_registry():
    return BadgerRegistry.deploy({'from': accounts[0]})
