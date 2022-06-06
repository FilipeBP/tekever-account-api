from typing import List

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from config import settings
from model.transaction_model import Transaction
from repository.orm.schema import TransactionOrm
from .transaction_abstract_repository import TransactionAbstractRepository


class TransactionOrmRepository(TransactionAbstractRepository):
    def __init__(self):
        self.engine = create_engine(
            f'sqlite:///{settings.SQLITE_PATH}'
        )

        self.session = Session(self.engine)

    def create(self, transaction_info: Transaction, external_session=None):
        session = external_session or self.session

        transaction = TransactionOrm(**transaction_info.dict())
        session.add(transaction)
        session.commit() if not external_session else None

    def get(self, account_id: str) -> List[Transaction]:
        transaction_obj = self.session.query(TransactionOrm).\
            filter(TransactionOrm.account_id == account_id).\
            all()

        return [Transaction.parse_obj(obj.__dict__) for obj in transaction_obj]
