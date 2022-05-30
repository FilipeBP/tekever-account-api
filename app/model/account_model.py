from datetime import datetime

from pydantic import BaseModel, Field


class Account(BaseModel):
    client_id: str = Field()
    account_id: str = Field()
    credit: float = Field()
    created_at: datetime = Field()
    updated_at: datetime = Field()
