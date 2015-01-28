# -*- coding: utf-8 -*-
import hashlib
from decimal import Decimal, InvalidOperation
from dateutil.parser import parse


class InvalidTransaction(Exception):
    pass


class RawTransaction(object):
    date = None
    description = None
    amount = None
    checksum = None

    """docstring for Transaction"""
    def __init__(self, **kwargs):
        self.kwargs = kwargs
        self._determine_types()

    def _determine_types(self):
        """
            Will either be a date, a decimal, or a string
            covering off when, what and amount. Uber basic
            at the moment

            #TODO: Make this less brittle

        """
        try:
            self.date = parse(self.kwargs.get('date'))
            self.description = self.kwargs.get('description').strip()
            self.amount = Decimal(self.kwargs.get('amount'))
            self.checksum = hashlib.md5(u''.join(self.kwargs.values())
                                        .encode('utf-8')).digest()
        except (ValueError, InvalidOperation) as e:
            raise InvalidTransaction("Can't make a transaction from {0} - {1}"
                                     .format(self.kwargs, e))
