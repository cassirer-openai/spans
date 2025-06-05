from datetime import date, datetime, timedelta

import pytest

import spans


@pytest.fixture(autouse=True)
def doctest_fixture(doctest_namespace):
    for attr in spans.__all__:
        doctest_namespace[attr] = getattr(spans, attr)

    doctest_namespace["date"] = date
    doctest_namespace["datetime"] = datetime
    doctest_namespace["timedelta"] = timedelta
