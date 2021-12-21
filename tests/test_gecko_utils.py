import pytest
import responses

from badger_utils.coingecko_utils import address_to_id
from badger_utils.coingecko_utils import fetch_daily_twap
from badger_utils.coingecko_utils import fetch_usd_price
from badger_utils.coingecko_utils import fetch_usd_price_eth
from badger_utils.coingecko_utils import fetch_usd_value
from badger_utils.registry import registry

GECKO_GENERIC_RESPONSE = {'market_data': {'current_price': {'usd': 3500.12}}}


@pytest.mark.parametrize(
    "address, id",
    [
        (registry.tokens.wbtc, "wrapped-bitcoin"),
        (registry.tokens.badger, "badger-dao"),
        (registry.tokens.digg, "digg"),
        (registry.tokens.cvx, "convex-finance"),
        (registry.tokens.crv, "curve-dao-token"),
        (registry.tokens.cvxCrv, "convex-crv"),
        (registry.tokens.sushi, "sushi"),
        (registry.tokens.xSushi, "xsushi"),
        (registry.tokens.bbadger, "badger-sett-badger"),
        (registry.tokens.spell, "spell-token"),
        (registry.tokens.renbtc, "renbtc"),
        (registry.tokens.sbtc, "sbtc"),
        (registry.tokens.tbtc, "tbtc"),
        (registry.tokens.bbtc, "binance-wrapped-btc"),
        (registry.tokens.obtc, "boringdao-btc"),
        (registry.tokens.pbtc, "ptokens-btc"),
        (registry.tokens.hbtc, "huobi-btc"),
        (registry.tokens.meta, "meta"),
        (registry.tokens.bnb, "binance-coin"),
        (registry.tokens.matic, "polygon"),
        (registry.tokens.aave, "aave"),
        (registry.tokens.comp, "compound"),
        (registry.tokens.ohm, "olympus"),
        (registry.tokens.swpr, "swapr"),
    ]
)
def test_token_to_id(address, id):
    assert address_to_id(address) == id


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
    assert fetch_usd_price("0x3472a5a71965499acd81997a54bba8d852c6e53d") == 3500.12


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
