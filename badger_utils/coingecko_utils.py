from typing import Dict
from typing import Optional
from typing import Union

import requests
from brownie import web3
from requests import HTTPError

from badger_utils.registry import registry


TOKEN_TO_ID_MAP = {
    web3.toChecksumAddress(registry.tokens.wbtc): "wrapped-bitcoin",
    web3.toChecksumAddress(registry.tokens.badger): "badger-dao",
    web3.toChecksumAddress(registry.tokens.digg): "digg",
    web3.toChecksumAddress(registry.tokens.cvx): "convex-finance",
    web3.toChecksumAddress(registry.tokens.crv): "curve-dao-token",
    web3.toChecksumAddress(registry.tokens.cvxCrv): "convex-crv",
    web3.toChecksumAddress(registry.tokens.sushi): "sushi",
    web3.toChecksumAddress(registry.tokens.xSushi): "xsushi",
    web3.toChecksumAddress(registry.tokens.bbadger): "badger-sett-badger",
    web3.toChecksumAddress(registry.tokens.spell): "spell-token",
    web3.toChecksumAddress(registry.tokens.renbtc): "renbtc",
    web3.toChecksumAddress(registry.tokens.sbtc): "sbtc",
    web3.toChecksumAddress(registry.tokens.tbtc): "tbtc",
    web3.toChecksumAddress(registry.tokens.bbtc): "binance-wrapped-btc",
    web3.toChecksumAddress(registry.tokens.obtc): "boringdao-btc",
    web3.toChecksumAddress(registry.tokens.pbtc): "ptokens-btc",
    web3.toChecksumAddress(registry.tokens.hbtc): "huobi-btc",
    web3.toChecksumAddress(registry.tokens.meta): "meta",
    web3.toChecksumAddress(registry.tokens.bnb): "binance-coin",
    web3.toChecksumAddress(registry.tokens.matic): "polygon",
    web3.toChecksumAddress(registry.tokens.aave): "aave",
    web3.toChecksumAddress(registry.tokens.comp): "compound",
    web3.toChecksumAddress(registry.tokens.ohm): "olympus",
    web3.toChecksumAddress(registry.tokens.swpr): "swapr",
}


def address_to_id(token_address: str) -> Union[str, bool]:
    checksummed = web3.toChecksumAddress(token_address)
    return TOKEN_TO_ID_MAP.get(checksummed, False)


def fetch_usd_value(token_address: str, amount: int) -> float:
    price = fetch_usd_price(token_address)
    return price * amount


def fetch_daily_twap(token_address: str) -> Optional[Dict]:
    response = requests.get(
        f"https://api.coingecko.com/api/v3/coins/{address_to_id(token_address)}",
        params="tickers=true&community_data=false&developer_data=false&sparkline=false"
    )
    try:
        response.raise_for_status()
    except HTTPError:
        return
    data = response.json()
    market_data = data["market_data"]
    return market_data


def fetch_usd_price(token_address: str) -> Optional[float]:
    response = requests.get(
        f"https://api.coingecko.com/api/v3/coins/{address_to_id(token_address)}",
        params="tickers=false&community_data=false&developer_data=false&sparkline=false"
    )
    try:
        response.raise_for_status()
    except HTTPError:
        return
    data = response.json()
    usd_price = data["market_data"]["current_price"]["usd"]
    return usd_price


def fetch_usd_price_eth() -> Optional[float]:
    response = requests.get(
        "https://api.coingecko.com/api/v3/coins/ethereum",
        params="?tickers=false&community_data=false&developer_data=false&sparkline=false"
    )
    try:
        response.raise_for_status()
    except HTTPError:
        return
    data = response.json()
    usd_price = data["market_data"]["current_price"]["usd"]
    return usd_price
