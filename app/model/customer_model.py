import uuid
from typing import List

from pydantic import BaseModel, Field

from model.transaction_model import Transaction


class CustomerIn(BaseModel):
    name: str = Field(title='Customer name', example='José')
    surname: str = Field(None, title='Customer surname', example='Silva')


class Customer(CustomerIn):
    id: str = Field(title='Customer ID', example=f'{str(uuid.uuid4())}')

    @classmethod
    def create_customer(cls, customer_info: CustomerIn):
        return cls(
            id=str(uuid.uuid4()),
            **customer_info.dict()
        )


class CustomerOut(Customer):
    balance: float = Field(0.0, description='Accounts total amount', example=1000)
    transactions: List[Transaction] = Field(description='Every transaction done by the customer')
