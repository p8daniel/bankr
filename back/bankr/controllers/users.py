from bankr.errors.not_found import UserNotFoundError
from bankr.models.user import User


def get_user_by_name(user_name):
    db_user = User.get_or_none(username=user_name)
    if db_user is None:
        raise UserNotFoundError(user_name)
    else:
        return db_user
