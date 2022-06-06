from fastapi import FastAPI
from controller.customer_controller import router as customer_router
from repository import customer_repository
from repository.orm.schema import Base

app = FastAPI(
    title='Account API'
)

app.include_router(customer_router, prefix='/customer', tags=['Customer'])


@app.on_event('startup')
def create_db():
    Base.metadata.create_all(customer_repository.engine)
