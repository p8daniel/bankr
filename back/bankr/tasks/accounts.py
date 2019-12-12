from weboob.core import Weboob

from bankr.core import logger
from bankr.models.account import Account

from . import celery


@celery.task
def retrieve_accounts():
    w = Weboob()
    w.load_backends(names=('fakebank',))

    fake_bank = w.get_backend('fakebank')
    accounts = fake_bank.iter_accounts()
    for account in accounts:
        logger.info(f'{account.label} - {account.balance}')
        Account.create(id=account.id, label=account.label, balance=account.balance, bank='fakebank')
