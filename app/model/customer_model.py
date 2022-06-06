import uuid
from typing import List

from pydantic import BaseModel, Field

from model.transaction_model import Transaction


class CustomerIn(BaseModel):
    name: str = Field()
    surname: str = Field()


class Customer(CustomerIn):
    id: str = Field()

    @classmethod
    def create_customer(cls, customer_info: CustomerIn):
        return cls(
            id=str(uuid.uuid4()),
            **customer_info.dict()
        )


class CustomerOut(Customer):
    balance: float = Field(0.0)
    transactions: List[Transaction]
