from fastapi import FastAPI
from controller.customer_controller import router as customer_router
from repository import customer_repository
from repository.orm.schema import Base

description = """
Manipulates all data related to Customer and its accounts

## Customer

Its possible to create customers and read its info.

## Account

Regards all about account, from its creation to reading the transactions of a single account

## Improvements

* Update user info
* Delete accounts

_The API can integrate unit and integration tests easilly, however it wasn't implemented a mock database._
"""

app = FastAPI(
    title='Account API',
    version='0.0.1',
    description=description
)

app.include_router(customer_router, prefix='/customer', tags=['Customer'])


@app.on_event('startup')
def create_db():
    Base.metadata.create_all(customer_repository.engine)
