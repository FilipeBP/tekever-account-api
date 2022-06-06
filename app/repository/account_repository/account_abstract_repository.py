from abc import ABC, abstractmethod
from typing import List

from model.account_model import Account


class AccountAbstractRepository(ABC):

    @abstractmethod
    def create(self, account_info: Account):
        raise NotImplementedError

    @abstractmethod
    def get(self, client_id: str, account_id: str) -> Account:
        raise NotImplementedError

    @abstractmethod
    def get_by_client(self, client_id: str) -> List[Account]:
        raise NotImplementedError

    @abstractmethod
    def update(self, account_id: str, account_info: Account):
        raise NotImplementedError

    @abstractmethod
    def delete(self, client_id: str) -> None:
        raise NotImplementedError
