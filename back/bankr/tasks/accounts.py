from weboob.core import Weboob

from bankr.core import logger
from bankr.models.account import Account
from bankr.models.bank import Bank
from bankr.models.user import User

from . import celery


@celery.task
def retrieve_accounts():
    w = Weboob()
    w.load_backends(names=('fakebank',))

    fake_bank = w.get_backend('fakebank')
    accounts = fake_bank.iter_accounts()
    the_user = User.get_or_none(username='foo')
    if the_user is None:
        the_user = User.create(username='foo', password='bar')
    the_bank = Bank.get_or_none(name='fakebank')
    if the_bank is None:
        the_bank = Bank.create(name='fakebank')
    for account in accounts:
        logger.info(f'{account.label} - {account.balance}')
        Account.create(id=account.id, label=account.label, balance=account.balance, bank=the_bank, user=the_user)
