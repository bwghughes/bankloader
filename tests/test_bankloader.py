#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_bankloader
----------------------------------

Tests for `bankloader` module.
"""

import datetime
from decimal import Decimal
from bankloader import RawTransaction


def test_raw_transaction_looks_good():
    t = RawTransaction(*['21/3/2014', 'MCDONALDS', '4.52'])
    assert isinstance(t.date, datetime.datetime)
    assert t.description == 'MCDONALDS'
    assert isinstance(t.amount, Decimal)
    assert t.checksum

def test_fails_with_invalid_or_incorrect_data():
    pass
