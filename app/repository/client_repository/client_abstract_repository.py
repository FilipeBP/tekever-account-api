from abc import ABC, abstractmethod

from model.client_model import ClientIn, Client


class ClientAbstractRepository(ABC):

    @abstractmethod
    def create(self, client_info: ClientIn):
        raise NotImplementedError

    @abstractmethod
    def get(self, client_id: str) -> Client:
        raise NotImplementedError

    @abstractmethod
    def update(self, client_id: str, client_info: ClientIn):
        raise NotImplementedError

    @abstractmethod
    def delete(self, client_id: str) -> None:
        raise NotImplementedError
