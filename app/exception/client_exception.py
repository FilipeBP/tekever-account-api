from fastapi import HTTPException


class ClientException(HTTPException):
    def __init__(self, status_code, detail):
        super(ClientException, self).__init__(status_code, detail)


class ClientNotFoundError(ClientException):
    def __init__(self, client_id: str):
        super(ClientNotFoundError, self).__init__(404, f"Client '{client_id}' not found.")
