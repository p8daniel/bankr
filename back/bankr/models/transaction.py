from peewee import *

from bankr.core import db

from .base_model import BaseModel
from .account import Account


class TransactionCategory(BaseModel):
    id = PrimaryKeyField()
    name = CharField()


class Transaction(BaseModel):
    account = ForeignKeyField(Account)
    label = CharField()
    amount = FloatField()
    date = CharField()
    vu = BooleanField()
    category = ForeignKeyField(TransactionCategory, null=True)

    def get_small_data(self):
        return {'id': self.id, 'account': self.account.label, 'bank':self.account.bank.name, 'label': self.label, 'amount': self.amount, 'date': self.date,
                'vu': self.vu, 'catégorie': self.category.name}


with db:
    TransactionCategory.create_table(fail_silently=True)
    Transaction.create_table(fail_silently=True)
