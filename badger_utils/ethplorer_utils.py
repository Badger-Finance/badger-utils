from typing import Dict
from typing import Optional

import requests


def get_top_token_holders(token_address: str, limit: Optional[int] = 50) -> Dict:
    holders_response = requests.get(
        f"https://api.ethplorer.io/getTopTokenHolders/{token_address}",
        params={"apiKey": "freekey", "limit": str(limit)},
    )
    holders_response.raise_for_status()
    return holders_response.json()
