from typing import List

from fastapi import APIRouter, Path, Depends

from model.account_model import Account, AccountIn
from model.customer_model import CustomerOut, CustomerIn
from service import customer_service, account_service

router = APIRouter()


@router.get(
    '/{customerId}',
    responses={
        200: {'model': CustomerOut}
    }
)
async def get_customer(
    customer_id: str = Path(..., alias='customerId')
):
    return customer_service.get_customer(customer_id)


@router.post(
    '/',
    responses={
        201: {'model': str}
    }
)
async def create_customer(
    customer_info: CustomerIn
):
    return customer_service.create_customer(customer_info)


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
async def get_accounts_by_customer(
    customer_id: str = Path(..., alias='customerId')
):
    return account_service.get_accounts_by_customer(customer_id)


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
