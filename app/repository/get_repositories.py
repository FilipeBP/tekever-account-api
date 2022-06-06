from config import settings

from .account_repository.account_abstract_repository import AccountAbstractRepository
from .account_repository.account_fake_repository import AccountFakeRepository
from .account_repository.account_orm_repository import AccountOrmRepository

from .customer_repository.customer_abstract_repository import CustomerAbstractRepository
from .customer_repository.client_fake_repository import CustomerFakeRepository
from .customer_repository.client_orm_repository import CustomerOrmRepository

from .transaction_repository.transaction_abstract_repository import TransactionAbstractRepository
from .transaction_repository.transaction_fake_repository import TransactionFakeRepository
from .transaction_repository.transaction_orm_repository import TransactionOrmRepository

from .repository_enum import CustomerRepositoryEnum, AccountRepositoryEnum, TransactionRepositoryEnum


def get_customer_repository(repository_name: CustomerRepositoryEnum) -> CustomerAbstractRepository:
    if repository_name == CustomerRepositoryEnum.ORM:
        return CustomerOrmRepository()
    return CustomerFakeRepository()


def get_account_repository(repository_name: AccountRepositoryEnum) -> AccountAbstractRepository:
    if repository_name == AccountRepositoryEnum.ORM:
        return AccountOrmRepository()
    return AccountFakeRepository()


def get_transaction_repository(repository_name: TransactionRepositoryEnum) -> TransactionAbstractRepository:
    if repository_name == TransactionRepositoryEnum.ORM:
        return TransactionOrmRepository()
    return TransactionFakeRepository()


customer_repository = get_customer_repository(settings.CUSTOMER_REPOSITORY)
account_repository = get_account_repository(settings.ACCOUNT_REPOSITORY)
transaction_repository = get_transaction_repository(settings.TRANSACTION_REPOSITORY)
