#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_bankloader
----------------------------------

Tests for `bankloader` module.
"""

import datetime
from decimal import Decimal
from bankloader import RawTransaction, InvalidTransaction

from pytest import raises, fixture


@fixture
def good_transaction():
    return RawTransaction(**{'date': '21/12/2014',
                             'description': 'TEST',
                             'amount': '21.20'})


@fixture
def bad_transaction():
    return RawTransaction(**{'date': '2112014',
                             'description': 'TEST',
                             'amount': 'bleugh'})


def test_raw_transaction_looks_good(good_transaction):
    assert isinstance(good_transaction.date, datetime.datetime)
    assert good_transaction.description == 'TEST'
    assert isinstance(good_transaction.amount, Decimal)
    assert good_transaction.checksum


def test_fails_with_invalid_or_incorrect_data():
    with raises(InvalidTransaction):
        RawTransaction(**{'date': '2112014',
                          'description':'TEST',
                          'amount': 'bleugh'})


