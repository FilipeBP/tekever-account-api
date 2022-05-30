from datetime import datetime

from pydantic import BaseModel, Field


class Transaction(BaseModel):
    id: str = Field()
    account_id: str = Field()
    amount: float = Field()
    created_at: datetime = Field()
