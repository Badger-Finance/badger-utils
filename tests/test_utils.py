import pytest
from brownie import accounts
from badger_utils.utils import approx
from badger_utils.utils import is_address_eoa
from badger_utils.utils import val


@pytest.mark.parametrize(
    "actual, expected, threshold",
    [
        (1, 1, 1), (90, 99, 99), (75, 100, 75)
    ]
)
def test_approx_match(actual, expected, threshold):
    assert approx(actual, expected, threshold)


@pytest.mark.parametrize(
    "actual, expected, threshold",
    [
        (1, 2, 1), (90, 99, 1), (75, 100, 25)
    ]
)
def test_approx_no_match(actual, expected, threshold):
    assert not approx(actual, expected, threshold)


@pytest.mark.parametrize(
    "amount, decimals, expected",
    [
        (0, 18, "0.000000000000000000"),
        (1000000000, 18, "0.000000001000000000"),
        (1000000000000000000, 18, "1.000000000000000000"),
    ]
)
def test_val(amount, decimals, expected):
    result = val(amount, decimals)
    assert result == expected


def test_is_address_eoa_accounts():
    for account in accounts:
        assert is_address_eoa(account.address)


def test_is_address_eoa_token(token):
    assert not is_address_eoa(token.address)
