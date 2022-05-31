from fastapi import APIRouter, Path

from model.client_model import ClientOut, ClientIn
from service import client_service

router = APIRouter()


@router.get(
    '/{customerId}',
    responses={
        200: {'model': ClientOut}
    }
)
async def get_client(
    customer_id: str = Path(..., alias='customerId')
):
    return client_service.get_client(customer_id)


@router.post(
    '/',
    responses={
        201: {'model': None}
    }
)
async def create_client(
    client_info: ClientIn
):
    return client_service.create_client(client_info)
