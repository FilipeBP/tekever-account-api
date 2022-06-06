import uuid
from datetime import datetime
from typing import List

from pydantic import BaseModel, Field, validator

from model.transaction_model import Transaction
from model.validators.account_validators import validate_balance


class AccountIn(BaseModel):
    additional_value: float = Field(0.0, description='Additional value to the account', example=2.05)


class Account(BaseModel):
    id: str = Field(title='Account ID', example=f'{str(uuid.uuid4())}')
    customer_id: str = Field(title='Customer ID', example=f'{str(uuid.uuid4())}')
    balance: float = Field(0.0, title='Account balance', description='Total amount of transactions of the account')
    created_at: datetime = Field(title='Creation datetime', example=f'{datetime.now()}')
    updated_at: datetime = Field(None, title='Update datetime', example=f'{datetime.now()}')

    @validator('balance', pre=True)
    def check_balance(cls, v):
        validate_balance(v)
        return v

    @classmethod
    def create_account(cls, customer_id: str, initial_credit: float):
        return cls(
            id=str(uuid.uuid4()),
            customer_id=customer_id,
            balance=initial_credit,
            created_at=datetime.now()
        )


class AccountOut(Account):
    transactions: List[Transaction] = Field(description='Every transaction related to the account')
