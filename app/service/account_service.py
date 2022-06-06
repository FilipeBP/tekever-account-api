from datetime import datetime
from typing import List

from model.account_model import Account
from repository import account_repository


def get_accounts_by_client(client_id: str) -> List[Account]:
    return account_repository.get_by_client(client_id)


def get_account(client_id: str, account_id: str) -> Account:
    return account_repository.get(client_id, account_id)


def create_account(client_id: str, initial_credit: float) -> dict:
    account = Account.create_account(client_id, initial_credit)
    account_id = account_repository.create(account)

    return {'detail': 'Account created', 'id': account_id, 'client_id': client_id}


def alter_account(customer_id: str, account_id: str, value: float):
    updated_at = datetime.now()
    account_repository.update(customer_id, account_id, value, updated_at)


def remove_account():
    pass
