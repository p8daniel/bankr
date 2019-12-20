from flask import request
from flask_restful import Resource

from bankr.controllers.accounts import get_accounts
from bankr.controllers.transactions import get_transactions, get_transaction_by_id, get_category_by_name


class Transactions(Resource):
    def get(self):
        bank = request.args.get('bank')
        account = request.args.get('account')
        transactions = [transaction.get_small_data() for transaction in get_transactions(bank, account)]
        return transactions


class Transaction(Resource):
    def post(self, transaction_id):
        transaction = get_transaction_by_id(transaction_id)
        seen = request.args.get('vu', default=None) in ('true', 'True')
        set_category = request.args.get('category', None)
        if seen is not None:
            transaction.vu = seen
            transaction.save()
        if set_category is not None:
            category = get_category_by_name(set_category)
            transaction.category = category

        return transaction.get_small_data()
