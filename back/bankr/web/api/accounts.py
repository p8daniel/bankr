from flask import request
from flask_restful import Resource

from bankr.controllers.accounts import get_accounts
from bankr.controllers.transactions import get_num_transactions


class Accounts(Resource):
    def get(self):
        bank = request.args.get('bank')
        name = request.args.get('nom', None)
        max_amount = request.args.get('max_amount', None)
        ask_number_transactions = request.args.get('transactions') in ('true', 'True')
        accounts = []
        for account in get_accounts(bank, name, max_amount):
            account_data = account.get_small_data()
            if ask_number_transactions is True:
                account_data['number of transactions'] = get_num_transactions(account)
            accounts.append(account_data)
        # accounts = [account.get_small_data() for account in get_accounts(bank, name, max_amount)]

        return accounts
