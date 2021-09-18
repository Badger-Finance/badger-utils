from typing import Dict
from typing import Optional
from typing import Union

import requests
from brownie import web3
from requests import HTTPError

from badger_utils.registry import registry


def address_to_id(token_address: str) -> Union[str, bool]:
    checksummed = web3.toChecksumAddress(token_address)
    if checksummed == web3.toChecksumAddress(registry.tokens.wbtc):
        return "wrapped-bitcoin"
    if checksummed == web3.toChecksumAddress(registry.tokens.badger):
        return "badger-dao"
    if checksummed == web3.toChecksumAddress(registry.tokens.digg):
        return "digg"
    else:
        assert False


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
