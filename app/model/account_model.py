import uuid
from datetime import datetime
from typing import List

from pydantic import BaseModel, Field, validator

from model.transaction_model import Transaction
from model.validators.account_validators import validate_balance


class AccountIn(BaseModel):
    additional_value: float = Field(0.0)


class Account(BaseModel):
    id: str = Field()
    customer_id: str = Field()
    balance: float = Field(0.0)
    created_at: datetime = Field()
    updated_at: datetime = Field(None)

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
    transactions: List[Transaction] = Field()
