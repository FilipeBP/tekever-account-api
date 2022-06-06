import uuid
from datetime import datetime

from pydantic import BaseModel, Field


class Transaction(BaseModel):
    id: int = Field(None)
    account_id: str = Field()
    amount: float = Field()
    created_at: datetime = Field()

    @classmethod
    def create_transaction(cls, account_id: str, amount: float):
        return cls(
            account_id=account_id,
            amount=amount,
            created_at=datetime.now()
        )
