from abc import ABC, abstractmethod
from typing import List

from model.account_model import Account


class AccountAbstractRepository(ABC):

    @abstractmethod
    def create(self, account_info: Account):
        raise NotImplementedError

    @abstractmethod
    def get(self, customer_id: str, account_id: str) -> Account:
        raise NotImplementedError

    @abstractmethod
    def get_by_customer(self, customer_id: str) -> List[Account]:
        raise NotImplementedError

    @abstractmethod
    def update(self, account_id: str, account_info: Account):
        raise NotImplementedError

    @abstractmethod
    def delete(self, customer_id: str) -> None:
        raise NotImplementedError
