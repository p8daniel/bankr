from peewee import *

from bankr.core import db

from .base_model import BaseModel
from .account import Account


class Transaction(BaseModel):
    account = ForeignKeyField(Account)
    label = CharField()
    amount = FloatField()
    date =CharField()


with db:
    Transaction.create_table(fail_silently=True)
