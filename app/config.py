import os
from functools import lru_cache

from pydantic import BaseSettings, Field

from repository.repository_enum import ClientRepositoryEnum

DB_PATH = f'{os.getcwd()}/db.sqlite'


class Settings(BaseSettings):
    SQLITE_PATH: str = Field(DB_PATH, description='Database path used by sqlite')
    CLIENT_REPOSITORY: ClientRepositoryEnum = Field(ClientRepositoryEnum.ORM,
                                                    description='Repository used by client domain')

    class Config:
        env_file = os.getenv('ENV_FILE', '../.env')


@lru_cache()
def get_settings():
    return Settings()


settings = get_settings()
