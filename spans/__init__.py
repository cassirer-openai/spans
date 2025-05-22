"""
This module provides one dimensional continuous set support for python.

Python has a wonderful set class, it does however not handle continuous sets
between two endpoints. This module tries to mitigate that. The ranges' behavior
are modeled after PostgresSQL 9.2's range types. Deviating from PostgresSQL's
behavior is considered a bug.

In addition to the range types there are range sets. A range set is can be viewed
as a mutable list of ranges. A set enables discontinuous chunks to be grouped
together.
"""


__version__ = "1.1.1"


__all__ = [
    "intrange",
    "floatrange",
    "strrange",
    "daterange",
    "datetimerange",
    "timedeltarange",
    "PeriodRange",
    "intrangeset",
    "floatrangeset",
    "strrangeset",
    "daterangeset",
    "datetimerangeset",
    "timedeltarangeset",
]


from .settypes import *
from .types import *
