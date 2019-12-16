from weboob.capabilities.bank import CapBank
from weboob.core import Weboob

from bankr.core import logger
from bankr.models.account import Account
from bankr.models.bank import Bank
from . import celery


@celery.task
def retrieve_accounts():
    w = Weboob()
    w.load_backends(caps=(CapBank,))

    for bank in Bank.select():
        bank_backend = w.get_backend(bank.name)

        accounts = bank_backend.iter_accounts()
        for account in accounts:
            logger.info(f'[Accounts] Retrieving account {account.label} - {account.balance} from {bank.name}')

            db_account = Account.get_or_none(bank=bank, account_id=account.id)
            if db_account is None:
                db_account = Account.create(bank=bank, account_id=account.id, user=1, label=account.label,
                                            balance=account.balance)
            else:
                db_account.label = account.label
                db_account.balance = account.balance
                db_account.save()
