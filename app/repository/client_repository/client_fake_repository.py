from model.client_model import ClientIn, Client
from .client_abstract_repository import ClientAbstractRepository


class ClientFakeRepository(ClientAbstractRepository):
    def create(self, client_info: ClientIn):
        pass

    def get(self, client_id: str) -> Client:
        pass

    def update(self, client_id: str, client_info: ClientIn):
        pass

    def delete(self, client_id: str) -> None:
        pass
