import pytest
import responses
from requests import HTTPError

from badger_utils.ethplorer_utils import get_top_token_holders

ETHPLORER_TOP_TOKEN_HOLDERS_GENERIC_RESPONSE = [
    {'address': '0x4441776e6a5d61fa024a5117bfc26b953ad1f425', 'balance': 7.35e+24, 'share': 35},
    {'address': '0xbd9c69654b8f3e5978dfd138b00cb0be29f28ccf', 'balance': 2.8391798793070636e+24,
     'share': 13.52},
    {'address': '0x394dcfbcf25c5400fcc147ebd9970ed34a474543', 'balance': 1.3700030213705368e+24,
     'share': 6.52}]


@responses.activate
def test_get_top_token_holders__happy_path():
    responses.add(
        responses.GET,
        "https://api.ethplorer.io/getTopTokenHolders/0x3472A5A71965499acd81997a54BBA8D852C6E53d",
        json=ETHPLORER_TOP_TOKEN_HOLDERS_GENERIC_RESPONSE, status=200
    )
    # Badger token top holders
    response = get_top_token_holders("0x3472A5A71965499acd81997a54BBA8D852C6E53d")
    assert response == ETHPLORER_TOP_TOKEN_HOLDERS_GENERIC_RESPONSE


@responses.activate
def test_get_top_token_holders__unhappy_path():
    responses.add(
        responses.GET,
        "https://api.ethplorer.io/getTopTokenHolders/0x3472A5A71965499acd81997a54BBA8D852C6E53d",
        json={}, status=404
    )
    with pytest.raises(HTTPError):
        get_top_token_holders("0x3472A5A71965499acd81997a54BBA8D852C6E53d")
