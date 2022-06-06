from typing import List

from fastapi import APIRouter, Path, Depends

from model.account_model import Account, AccountIn
from model.client_model import ClientOut, ClientIn
from service import client_service, account_service

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
        201: {'model': str}
    }
)
async def create_client(
    client_info: ClientIn
):
    return client_service.create_client(client_info)


@router.post(
    '/{customerId}/accounts',
    responses={
        201: {'model': str}
    }
)
async def create_account(
    body: AccountIn,
    customer_id: str = Path(..., alias='customerId')
):
    return account_service.create_account(customer_id, body.additional_value)


@router.patch(
    '/{customerId}/accounts/{accountId}',
    responses={
        201: {'model': str}
    }
)
async def create_account(
    body: AccountIn,
    customer_id: str = Path(..., alias='customerId'),
    account_id: str = Path(..., alias='accountId')
):
    return account_service.alter_account(customer_id, account_id, body.additional_value)


@router.get(
    '/{customerId}/accounts',
    responses={
        200: {'model': List[Account]}
    }
)
async def get_accounts_by_client(
    customer_id: str = Path(..., alias='customerId')
):
    return account_service.get_accounts_by_client(customer_id)


@router.get(
    '/{customerId}/accounts/{accountId}',
    responses={
        200: {'model': List[Account]}
    }
)
async def get_account(
    customer_id: str = Path(..., alias='customerId'),
    account_id: str = Path(..., alias='accountId')
):
    return account_service.get_account(customer_id, account_id)
