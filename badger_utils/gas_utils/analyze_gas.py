import os
from time import time
from typing import Dict
from typing import List
from typing import Optional

import numpy as np
from dotmap import DotMap
from elasticsearch import Elasticsearch

from badger_utils.constants import HISTORICAL_MAINNET_ELASTIC_URL
from badger_utils.constants import NUMBER_OF_BINS


def is_outlier(points: np.array, thresh=3.5) -> bool:
    """
    Returns a boolean array with True if points are outliers and False
    otherwise.

    Parameters:
    -----------
        points : A numobservations by numdimensions array of observations
        thresh : The modified z-score to use as a threshold. Observations with
            a modified z-score (based on the median absolute deviation) greater
            than this value will be classified as outliers.

    Returns:
    --------
        mask : A numobservations-length boolean array.

    References:
    ----------
        Boris Iglewicz and David Hoaglin (1993), "Volume 16: How to Detect and
        Handle Outliers", The ASQC Basic References in Quality Control:
        Statistical Techniques, Edward F. Mykytka, Ph.D., Editor.
    """
    if len(points.shape) == 1:
        points = points[:, None]
    median = np.median(points, axis=0)
    diff = np.sum((points - median) ** 2, axis=-1)
    diff = np.sqrt(diff)
    med_abs_deviation = np.median(diff)

    modified_z_score = 0.6745 * diff / med_abs_deviation

    return modified_z_score > thresh


def fetch_gas_hour(network: str, hours=24) -> List[float]:
    """
    Fetch average hourly gas prices over the last specified hours
    """
    es = Elasticsearch(
        hosts=[network],
        http_auth=(os.environ.get("ANYBLOCK_EMAIL"), os.environ.get("ANYBLOCK_KEY")), timeout=180
    )
    now = int(time())
    seconds = hours * 3600
    data = es.search(
        index="tx",
        doc_type="tx",
        body={
            "_source": ["timestamp", "gasPrice.num"],
            "query": {
                "bool": {
                    "must": [
                        {"range": {"timestamp": {"gte": now - seconds, "lte": now}}}
                    ]
                }
            },
            "aggs": {
                "hour_bucket": {
                    "date_histogram": {
                        "field": "timestamp",
                        "interval": "1H",
                        "format": "yyyy-MM-dd hh:mm:ss",
                    },
                    "aggs": {"avgGasHour": {"avg": {"field": "gasPrice.num"}}},
                }
            },
        },
    )
    return [
        x["avgGasHour"]["value"]
        for x in data["aggregations"]["hour_bucket"]["buckets"]
        if x["avgGasHour"]["value"]
    ]


# fetch average gas prices per minute over the last specified minutes
def fetch_gas_min(network: str, minutes=60) -> List[float]:
    es = Elasticsearch(
        hosts=[network],
        http_auth=(os.environ.get("ANYBLOCK_EMAIL"), os.environ.get("ANYBLOCK_KEY")), timeout=180
    )
    now = int(time())
    seconds = minutes * 60
    data = es.search(
        index="tx",
        doc_type="tx",
        body={
            "_source": ["timestamp", "gasPrice.num"],
            "query": {
                "bool": {
                    "must": [
                        {"range": {"timestamp": {"gte": now - seconds, "lte": now}}}
                    ]
                }
            },
            "aggs": {
                "minute_bucket": {
                    "date_histogram": {
                        "field": "timestamp",
                        "interval": "1m",
                        "format": "yyyy-MM-dd hh:mm",
                    },
                    "aggs": {"avgGasMin": {"avg": {"field": "gasPrice.num"}}},
                }
            },
        },
    )
    return [
        x["avgGasMin"]["value"]
        for x in data["aggregations"]["minute_bucket"]["buckets"]
        if x["avgGasMin"]["value"]
    ]


def analyze_gas(options: Optional[Dict] = None) -> DotMap:
    if not options:
        options = {
            "timeframe": "minutes", "periods": 60
        }
    if not os.environ.get("ANYBLOCK_EMAIL") or not os.environ.get("ANYBLOCK_KEY"):
        # Could not fetch historical gas data
        return DotMap(
            mode=999999999999999999, median=999999999999999999, std=999999999999999999
        )

    # fetch data
    if options["timeframe"] == "minutes":
        gas_data = fetch_gas_min(HISTORICAL_MAINNET_ELASTIC_URL, options["periods"])
    else:
        gas_data = fetch_gas_hour(HISTORICAL_MAINNET_ELASTIC_URL, options["periods"])
    gas_data = np.array(gas_data)

    # remove outliers
    filtered_gas_data = gas_data[~is_outlier(gas_data)]

    # Create histogram
    counts, bins = np.histogram(filtered_gas_data, bins=NUMBER_OF_BINS)

    # Find most common gas price
    biggest_bin = 0
    biggest_index = 0
    for i, x in enumerate(counts):
        if x > biggest_bin:
            biggest_bin = x
            biggest_index = i

    midpoint = (bins[biggest_index] + bins[biggest_index + 1]) / 2

    if int(midpoint) == 0:
        # Could not fetch historical gas data
        return DotMap(
            mode=999999999999999999, median=999999999999999999, std=999999999999999999
        )

    # standard deviation
    standard_dev = np.std(filtered_gas_data, dtype=np.float64)

    # average
    median = np.median(filtered_gas_data, axis=0)

    return DotMap(mode=int(midpoint), median=int(median), std=int(standard_dev))
