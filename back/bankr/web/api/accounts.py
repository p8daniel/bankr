from flask import request
from flask_restful import Resource

from bankr.controllers.accounts import get_accounts


class Accounts(Resource):
    def get(self):
        bank = request.args.get('bank')
        accounts = [account.get_small_data() for account in get_accounts(bank)]

        return accounts
