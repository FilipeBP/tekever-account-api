import uuid
from datetime import datetime

from pydantic import BaseModel, Field


class Transaction(BaseModel):
    id: int = Field(None, title='Transaction ID', example=1)
    account_id: str = Field(title='Account ID', example=f'{str(uuid.uuid4())}')
    amount: float = Field(title='Amount')
    created_at: datetime = Field(title='Creation datetime', example=f'{datetime.now()}')

    @classmethod
    def create_transaction(cls, account_id: str, amount: float):
        return cls(
            account_id=account_id,
            amount=amount,
            created_at=datetime.now()
        )
