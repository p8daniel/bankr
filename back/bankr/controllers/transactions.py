from bankr.errors.not_found import BankNotFoundError, AccountNotFoundError
from bankr.models.transaction import Transaction
# from bankr.models.bank import Bank
from .accounts import get_accounts
from bankr.models.account import Account


def get_transactions(bank=None, account=None):

    retrieved_accounts = get_accounts(bank)

    for retrieved_account in retrieved_accounts:

        if retrieved_account.account_id == account:

            transactions = Transaction.select()
            if account is not None:
                db_account = Account.get_or_none(account_id=account)
                if db_account is None:
                    raise AccountNotFoundError(account)

                transactions = transactions.where(Transaction.account == db_account)
                return transactions


        else:
            raise AccountNotFoundError(account)
