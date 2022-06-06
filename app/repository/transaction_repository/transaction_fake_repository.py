from typing import List

from model.transaction_model import Transaction
from .transaction_abstract_repository import TransactionAbstractRepository


class TransactionFakeRepository(TransactionAbstractRepository):
    def create(self, transaction_info: Transaction):
        pass

    def get(self, account_id: str) -> List[Transaction]:
        pass
