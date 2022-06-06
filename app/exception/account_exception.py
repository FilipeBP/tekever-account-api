from fastapi import HTTPException


class AccountException(HTTPException):
    def __init__(self, status_code, detail):
        super(AccountException, self).__init__(status_code, detail)


class NegativeBalanceError(AccountException):
    def __init__(self):
        super(NegativeBalanceError, self).__init__(
            422,
            f"It's not possible to have an account with negative balance."
        )


class AccountNotFoundError(AccountException):
    def __init__(self, client_id: str, account_id: str):
        super(AccountNotFoundError, self).__init__(
            404,
            f"Account '{account_id}' for client '{client_id}' was not found."
        )
