import uuid

from pydantic import BaseModel, Field


class CustomerCreated(BaseModel):
    detail: str = Field('Customer created')
    id: str = Field(title='New customer ID', example=f'{str(uuid.uuid4())}')


class AccountCreated(BaseModel):
    detail: str = Field('Account created')
    id: str = Field(title='New account ID', example=f'{str(uuid.uuid4())}')
    customer_id: str = Field(title='Customer ID', example=f'{str(uuid.uuid4())}')
