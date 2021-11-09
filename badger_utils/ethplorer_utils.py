from typing import Dict

import requests


def get_top_token_holders(token_address: str) -> Dict:
    holders_response = requests.get(
        f"https://api.ethplorer.io/getTopTokenHolders/{token_address}",
        params={"apiKey": "freekey", "limit": "50"},
    )
    holders_response.raise_for_status()
    return holders_response.json()
