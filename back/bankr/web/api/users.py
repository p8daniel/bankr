from flask import request
from flask_restful import Resource

from bankr.controllers.accounts import get_accounts
from bankr.controllers.users import get_user_by_name


class User(Resource):
    def get(self, user):
        total_amount = 0
        db_user = get_user_by_name(user)
        db_accounts = get_accounts(db_user=db_user)
        for db_account in db_accounts:
            total_amount += db_account.balance
        return "Total balance of %s is %d" % (user, total_amount)
