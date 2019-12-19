from bankr.errors.not_found import BankNotFoundError, AccountNotFoundError
from bankr.models.transaction import Transaction
# from bankr.models.bank import Bank
from .accounts import get_accounts
from bankr.models.account import Account


def get_transactions(bank=None, account=None):

    transactions = Transaction.select()
    if bank is not None:
        retrieved_accounts = get_accounts(bank)
        if account is not None:
            db_account = Account.get_or_none(account_id=account)
            if db_account is None:
                raise AccountNotFoundError(account)
            else:
                transactions = transactions.where(Transaction.account == db_account)
        else:
            transactions = transactions.where(Transaction.account << retrieved_accounts)
    else:
        if account is not None:
            return []
    return transactions
