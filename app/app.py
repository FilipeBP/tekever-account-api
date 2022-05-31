from fastapi import FastAPI
from controller.client_controller import router as client_router
from repository import client_repository
from repository.orm_schema import Base

app = FastAPI(
    title='Account API'
)

app.include_router(client_router, prefix='/client', tags=['Client'])


@app.on_event('startup')
def create_db():
    Base.metadata.create_all(client_repository.engine)
