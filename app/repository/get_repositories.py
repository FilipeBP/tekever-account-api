from config import settings

from repository.account_repository.account_abstract_repository import AccountAbstractRepository
from repository.account_repository.account_fake_repository import AccountFakeRepository
from repository.account_repository.account_orm_repository import AccountOrmRepository

from repository.client_repository.client_abstract_repository import ClientAbstractRepository
from repository.client_repository.client_fake_repository import ClientFakeRepository
from repository.client_repository.client_orm_repository import ClientOrmRepository

from repository.transaction_repository.transaction_abstract_repository import TransactionAbstractRepository
from repository.transaction_repository.transaction_fake_repository import TransactionFakeRepository
from repository.transaction_repository.transaction_orm_repository import TransactionOrmRepository

from repository.repository_enum import ClientRepositoryEnum, AccountRepositoryEnum, TransactionRepositoryEnum


def get_client_repository(repository_name: ClientRepositoryEnum) -> ClientAbstractRepository:
    if repository_name == ClientRepositoryEnum.ORM:
        return ClientOrmRepository()
    return ClientFakeRepository()


def get_account_repository(repository_name: AccountRepositoryEnum) -> AccountAbstractRepository:
    if repository_name == AccountRepositoryEnum.ORM:
        return AccountOrmRepository()
    return AccountFakeRepository()


def get_transaction_repository(repository_name: TransactionRepositoryEnum) -> TransactionAbstractRepository:
    if repository_name == TransactionRepositoryEnum.ORM:
        return TransactionOrmRepository()
    return TransactionFakeRepository()


client_repository = get_client_repository(settings.CLIENT_REPOSITORY)
account_repository = get_account_repository(settings.ACCOUNT_REPOSITORY)
transaction_repository = get_transaction_repository(settings.TRANSACTION_REPOSITORY)
