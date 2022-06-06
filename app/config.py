import os
from functools import lru_cache

from pydantic import BaseSettings, Field

from repository.repository_enum import CustomerRepositoryEnum, AccountRepositoryEnum, TransactionRepositoryEnum

DB_PATH = f'{os.getcwd()}/db.sqlite'


class Settings(BaseSettings):
    SQLITE_PATH: str = Field(DB_PATH, description='Database path used by sqlite')

    # REPOSITORIES
    CUSTOMER_REPOSITORY: CustomerRepositoryEnum = Field(CustomerRepositoryEnum.ORM,
                                                        description='Repository used by customer domain')
    ACCOUNT_REPOSITORY: CustomerRepositoryEnum = Field(AccountRepositoryEnum.ORM,
                                                       description='Repository used by account domain')
    TRANSACTION_REPOSITORY: CustomerRepositoryEnum = Field(TransactionRepositoryEnum.ORM,
                                                           description='Repository used by transaction domain')

    class Config:
        env_file = os.getenv('ENV_FILE', '../.env')


@lru_cache()
def get_settings():
    return Settings()


settings = get_settings()
