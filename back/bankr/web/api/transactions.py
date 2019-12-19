from flask import request
from flask_restful import Resource

from bankr.controllers.accounts import get_accounts
from bankr.controllers.transactions import get_transactions


class Transactions(Resource):
    def get(self):
        bank = request.args.get('bank')
        account = request.args.get('account')
        transactions = [transaction.get_small_data() for transaction in get_transactions(bank, account)]

        return transactions
