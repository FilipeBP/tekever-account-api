from fastapi import HTTPException


class CustomerException(HTTPException):
    def __init__(self, status_code, detail):
        super(CustomerException, self).__init__(status_code, detail)


class CustomerNotFoundError(CustomerException):
    def __init__(self, client_id: str):
        super(CustomerNotFoundError, self).__init__(404, f"Client '{client_id}' not found.")
