from datetime import datetime

import pytest

from badger_utils.time_utils import days_to_seconds
from badger_utils.time_utils import hours_to_seconds
from badger_utils.time_utils import minutes_to_seconds
from badger_utils.time_utils import seconds_to_days
from badger_utils.time_utils import seconds_to_hours
from badger_utils.time_utils import seconds_to_minutes
from badger_utils.time_utils import to_timestamp
from badger_utils.time_utils import to_utc_date


@pytest.mark.parametrize(
    "days, days_in_seconds",
    [
        (3, 259200), (1, 86400), (10, 864000), (0.5, 43200)
    ]
)
def test_days_to_seconds(days, days_in_seconds):
    assert days_to_seconds(days) == days_in_seconds


@pytest.mark.parametrize(
    "hours, hours_in_seconds",
    [
        (3, 10800), (1, 3600), (10, 36000), (0.1, 360)
    ]
)
def test_hours_to_seconds(hours, hours_in_seconds):
    assert hours_to_seconds(hours) == hours_in_seconds


@pytest.mark.parametrize(
    "minutes, minutes_in_seconds",
    [
        (3, 180), (1, 60), (10, 600), (0.1, 6)
    ]
)
def test_minutes_to_seconds(minutes, minutes_in_seconds):
    assert minutes_to_seconds(minutes) == minutes_in_seconds


def test_to_utc_date():
    assert to_utc_date(1231231231) == "2009-01-06 08:40:31"


def test_to_timestamp():
    date_time_obj = datetime.strptime('18/09/19 01:55:19', '%d/%m/%y %H:%M:%S')
    assert type(to_timestamp(date_time_obj)) is int


@pytest.mark.parametrize(
    "seconds, minutes",
    [
        (180, 3), (60, 1), (600, 10), (6, 0.1)
    ]
)
def test_seconds_to_minutes(seconds, minutes):
    assert seconds_to_minutes(seconds) == minutes


@pytest.mark.parametrize(
    "seconds, days",
    [
        (259200, 3), (86400, 1), (864000, 10), (43200, 0.5)
    ]
)
def test_seconds_to_days(seconds, days):
    assert seconds_to_days(seconds) == days


@pytest.mark.parametrize(
    "seconds, hours",
    [
        (10800, 3), (3600, 1), (36000, 10), (360, 0.1)
    ]
)
def test_seconds_to_hours(seconds, hours):
    assert seconds_to_hours(seconds) == hours
