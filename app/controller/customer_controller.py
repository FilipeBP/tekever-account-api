from typing import List

from fastapi import APIRouter, Path, Response

from model.account_model import Account, AccountIn, AccountOut
from model.customer_model import CustomerOut, CustomerIn
from model.response_model import CustomerCreated, AccountCreated
from service import customer_service, account_service

router = APIRouter()


@router.get(
    '/{customerId}',
    description='Get all information regarding the customer',
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
    description='Create a new customer',
    status_code=201,
    responses={
        201: {'model': CustomerCreated}
    }
)
async def create_customer(
    customer_info: CustomerIn
):
    return customer_service.create_customer(customer_info)


@router.post(
    '/{customerId}/accounts',
    description='Create a new account with its initial balance',
    status_code=201,
    responses={
        201: {'model': AccountCreated}
    }
)
async def create_account(
    body: AccountIn,
    customer_id: str = Path(..., alias='customerId')
):
    return account_service.create_account(customer_id, body.additional_value)


@router.patch(
    '/{customerId}/accounts/{accountId}',
    description='Add or remove a specific amount of the account',
    responses={
        201: {'model': None}
    }
)
async def create_account(
    body: AccountIn,
    customer_id: str = Path(..., alias='customerId'),
    account_id: str = Path(..., alias='accountId')
):
    account_service.alter_account(customer_id, account_id, body.additional_value)

    return Response(status_code=201)


@router.get(
    '/{customerId}/accounts',
    description='Get all accounts by customer',
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
    description='Get a detailed report of a single account',
    responses={
        200: {'model': AccountOut}
    }
)
async def get_account(
    customer_id: str = Path(..., alias='customerId'),
    account_id: str = Path(..., alias='accountId')
):
    return account_service.get_account(customer_id, account_id)
