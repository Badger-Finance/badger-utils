import os

import pytest
from dotmap import DotMap

from badger_utils.gas_utils.analyze_gas import analyze_gas
from tests.anyblock_test_data import ANYBLOCK_HOUR_AGG_DATA
from tests.anyblock_test_data import ANYBLOCK_MINUTE_AGG_DATA


@pytest.fixture
def add_anyblock_env_vars():
    os.environ['ANYBLOCK_EMAIL'] = "test@gmail.com"
    os.environ['ANYBLOCK_KEY'] = "591aa4bb-a4ce"
    yield
    os.environ.pop('ANYBLOCK_EMAIL')
    os.environ.pop('ANYBLOCK_KEY')


def test_analyze_gas__no_anyblock():
    gas = analyze_gas()
    assert gas == DotMap(
        mode=999999999999999999, median=999999999999999999, std=999999999999999999
    )


# Do some tests with precalculated prepared data to make sure algorithm always returns same result
def test_analyze_gas__minutes_timefr(add_anyblock_env_vars, mocker):
    mocker.patch(
        "badger_utils.gas_utils.analyze_gas.Elasticsearch.search",
        return_value={'aggregations': ANYBLOCK_MINUTE_AGG_DATA}
    )
    gas = analyze_gas(options={
        "timeframe": "minutes", "periods": 60
    })
    assert gas == DotMap(mode=58206954286, median=65210339070, std=7954866432)


def test_analyze_gas__hours_timefr(add_anyblock_env_vars, mocker):
    mocker.patch(
        "badger_utils.gas_utils.analyze_gas.Elasticsearch.search",
        return_value={'aggregations': ANYBLOCK_HOUR_AGG_DATA}
    )
    gas = analyze_gas(options={
        "timeframe": "hours", "periods": 60
    })
    assert gas == DotMap(mode=74204968356, median=79020050213, std=23108079208)
