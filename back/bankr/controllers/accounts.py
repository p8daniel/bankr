from bankr.errors.not_found import BankNotFoundError
from bankr.models.account import Account
from bankr.models.bank import Bank


def get_accounts(bank=None, name=None, max_amount=None, db_user=None):
    accounts = Account.select()
    if name is not None:
        accounts = accounts.where(Account.label.contains(name))
    if max_amount is not None:
        accounts = accounts.where(Account.balance <= max_amount)

    if db_user is not None:
        accounts = accounts.where(Account.user == db_user)



    if bank is not None:
        db_bank = Bank.get_or_none(name=bank)
        if db_bank is None:
            raise BankNotFoundError(bank)

        accounts = accounts.where(Account.bank == db_bank)

    return accounts



