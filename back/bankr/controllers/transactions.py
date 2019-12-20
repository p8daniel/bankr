from bankr.errors.not_found import AccountNotFoundError, TransactionNotFoundError, TansactionCategoryNotFoundError
from bankr.models.transaction import Transaction, TransactionCategory
from .accounts import get_accounts
from bankr.models.account import Account


def get_transactions(bank=None, account=None):
    transactions = Transaction.select().order_by(Transaction.id)
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


def get_transaction_by_id(id):
    transaction = Transaction.get_or_none(id=id)
    if transaction is None:
        raise TransactionNotFoundError(id)

    return transaction

def get_category_by_name(name):
    category = TransactionCategory.get_or_none(name=name)
    if category is None:
        raise TansactionCategoryNotFoundError(name)
    return category

def get_num_transactions(db_account):
    return Transaction.select().where(Transaction.account == db_account).count()
