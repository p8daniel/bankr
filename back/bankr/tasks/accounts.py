from weboob.capabilities.bank import CapBank
from weboob.core import Weboob

from bankr.core import logger
from bankr.models.account import Account
from bankr.models.bank import Bank
from bankr.models.user import User
from . import celery


@celery.task
def retrieve_accounts():
    w = Weboob()
    w.load_backends(caps=(CapBank,))
    logger.info(w.backend_instances)

    the_user = User.get_or_none(username='foo')
    if the_user is None:
        the_user = User.create(username='foo', password='bar')

    the_bank = Bank.get_or_none(name='fakebank')
    if the_bank is None:
        Bank.create(name='fakebank')

    for bank in Bank.select():

        bank_backend = w.get_backend(bank.name)
        # bank_backend = w.get_backend('fakebank')
        accounts = bank_backend.iter_accounts()

        for account in accounts:
            logger.info(f'[Accounts] Retrieving account {account.label} - {account.balance} from {bank.name}')

            db_account = Account.get_or_none(bank=bank, account_id=account.id)
            if db_account is None:
                db_account = Account.create(bank=bank, account_id=account.id, user=the_user, label=account.label,
                                            balance=account.balance)
            else:
                db_account.label = account.label
                db_account.balance = account.balance
                db_account.save()
