from bankr.errors.not_found import BankNotFoundError
from bankr.models.account import Account
from bankr.models.bank import Bank


def get_accounts(bank=None):
    accounts = Account.select()
    if bank is not None:
        db_bank = Bank.get_or_none(name=bank)
        if db_bank is None:
            raise BankNotFoundError(bank)

        accounts = accounts.where(Account.bank == db_bank)

    return accounts
