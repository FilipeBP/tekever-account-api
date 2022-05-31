from config import settings
from .client_repository.client_abstract_repository import ClientAbstractRepository
from .client_repository.client_fake_repository import ClientFakeRepository
from .client_repository.client_orm_repository import ClientOrmRepository
from .repository_enum import ClientRepositoryEnum


def get_client_repository(repository_name: ClientRepositoryEnum) -> ClientAbstractRepository:
    if repository_name == ClientRepositoryEnum.ORM:
        return ClientOrmRepository()
    return ClientFakeRepository()


client_repository = get_client_repository(settings.CLIENT_REPOSITORY)
