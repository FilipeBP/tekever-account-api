from abc import ABC, abstractmethod
from typing import List

from model.transaction_model import Transaction


class TransactionAbstractRepository(ABC):

    @abstractmethod
    def create(self, transaction_info: Transaction):
        raise NotImplementedError

    @abstractmethod
    def get(self, account_id: str) -> List[Transaction]:
        raise NotImplementedError

