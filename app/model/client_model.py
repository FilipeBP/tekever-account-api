import uuid
from typing import List

from pydantic import BaseModel, Field

from model.transaction_model import Transaction


class ClientIn(BaseModel):
    name: str = Field()
    surname: str = Field()


class Client(ClientIn):
    id: str = Field()

    @classmethod
    def create_client(cls, client_info: ClientIn):
        return Client(
            id=str(uuid.uuid4()),
            **client_info.dict()
        )


class ClientOut(Client):
    balance: float = Field(0.0)
    transactions: List[Transaction]
