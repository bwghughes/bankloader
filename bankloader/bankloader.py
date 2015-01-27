# -*- coding: utf-8 -*-
import md5
from decimal import Decimal
from dateutil.parser import parse


class RawTransaction(object):
    date = None
    description = None
    amount = None
    checksum = None

    """docstring for Transaction"""
    def __init__(self, *args):
        self.args = args
        self._determine_types()

    def _determine_types(self):
        """
            Will either be a date, a decimal, or a string
            covering off when, what and amount. Uber basic
            at the moment

            #TODO: Make this less brittle

        """
        self.date = parse(self.args[0])
        self.description = self.args[1].strip()
        self.amount = Decimal(self.args[2])
        self.checksum = md5.new(''.join(self.args)).digest()
