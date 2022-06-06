from exception.account_exception import NegativeBalanceError


def validate_balance(credit: float):
    if credit < 0:
        raise NegativeBalanceError()
