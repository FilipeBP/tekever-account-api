from pydantic import BaseModel, Field


class Client(BaseModel):
    id: str = Field()
    name: str = Field()
    surname: str = Field()
    balance: float = Field()
    