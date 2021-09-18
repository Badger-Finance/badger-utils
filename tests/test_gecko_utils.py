import responses

from badger_utils.coingecko_utils import fetch_daily_twap
from badger_utils.coingecko_utils import fetch_usd_price
from badger_utils.coingecko_utils import fetch_usd_price_eth
from badger_utils.coingecko_utils import fetch_usd_value

GECKO_GENERIC_RESPONSE = {'market_data': {'current_price': {'usd': 3500.12}}}


@responses.activate
def test_fetch_usd_price_eth__happy_path():
    responses.add(responses.GET, 'https://api.coingecko.com/api/v3/coins/ethereum',
                  json=GECKO_GENERIC_RESPONSE, status=200)
    assert fetch_usd_price_eth() == 3500.12


@responses.activate
def test_fetch_usd_price_eth__unhappy_path():
    responses.add(responses.GET, 'https://api.coingecko.com/api/v3/coins/ethereum',
                  json={'error': 'error'}, status=500)
    assert not fetch_usd_price_eth()


@responses.activate
def test_fetch_usd_price__happy_path():
    responses.add(
        responses.GET,
        'https://api.coingecko.com/api/v3/coins/badger-dao'
        '?tickers=false&community_data=false&developer_data=false&sparkline=false',
        json=GECKO_GENERIC_RESPONSE, status=200)
    assert fetch_usd_price("0x3472a5a71965499acd81997a54bba8d852c6e53d") == 20.12


@responses.activate
def test_fetch_usd_price__unhappy_path():
    responses.add(
        responses.GET,
        'https://api.coingecko.com/api/v3/coins/badger-dao'
        '?tickers=false&community_data=false&developer_data=false&sparkline=false',
        json=GECKO_GENERIC_RESPONSE, status=500)
    assert not fetch_usd_price("0x3472a5a71965499acd81997a54bba8d852c6e53d")


@responses.activate
def test_fetch_daily_twap__happy_path():
    responses.add(
        responses.GET,
        "https://api.coingecko.com/api/v3/coins/badger-dao?"
        "tickers=true&community_data=false&developer_data=false&sparkline=false",
        json=GECKO_GENERIC_RESPONSE, status=200)
    assert fetch_daily_twap(
        "0x3472a5a71965499acd81997a54bba8d852c6e53d") == GECKO_GENERIC_RESPONSE['market_data']


@responses.activate
def test_fetch_daily_twap__unhappy_path():
    responses.add(
        responses.GET,
        "https://api.coingecko.com/api/v3/coins/badger-dao?"
        "tickers=true&community_data=false&developer_data=false&sparkline=false",
        json={}, status=500)
    assert not fetch_daily_twap("0x3472a5a71965499acd81997a54bba8d852c6e53d")


@responses.activate
def test_fetch_usd_value():
    responses.add(
        responses.GET,
        'https://api.coingecko.com/api/v3/coins/badger-dao'
        '?tickers=false&community_data=false&developer_data=false&sparkline=false',
        json=GECKO_GENERIC_RESPONSE, status=200)
    # Check price for 10 ETH coins
    assert fetch_usd_value("0x3472a5a71965499acd81997a54bba8d852c6e53d", 10) == 3500.12 * 10
