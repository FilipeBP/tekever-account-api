from datetime import datetime
from decimal import Decimal
from functools import wraps
from typing import List

from sqlalchemy import create_engine, event
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from config import settings
from exception.account_exception import NegativeBalanceError, AccountNotFoundError
from model.account_model import Account, AccountOut
from model.transaction_model import Transaction
from .account_abstract_repository import AccountAbstractRepository
from repository.orm.schema import AccountOrm, TransactionOrm


def catch_sqlalchemy_exception(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except IntegrityError:
            raise NegativeBalanceError()
    return wrapper


class AccountOrmRepository(AccountAbstractRepository):
    def __init__(self):
        self.engine = create_engine(
            f'sqlite:///{settings.SQLITE_PATH}'
        )

        self.session = Session(self.engine)

    def create(self, account_info: Account):
        account = AccountOrm(**account_info.dict(exclude_none=True))

        self.session.add(account)
        self.session.flush()

        return account_info.id

    def get(self, client_id: str, account_id: str) -> Account:
        account_obj = self.session.query(AccountOrm, TransactionOrm).\
            join(TransactionOrm, AccountOrm.id == TransactionOrm.account_id, isouter=True).\
            filter(
                AccountOrm.client_id == client_id,
                AccountOrm.id == account_id
            ).all()

        if not account_obj:
            raise AccountNotFoundError(client_id, account_id)

        transactions = [Transaction(**obj[1].__dict__) for obj in account_obj] if account_obj[0][1] else []
        return AccountOut(transactions=transactions, **account_obj[0][0].__dict__)

    def get_by_client(self, client_id: str) -> List[Account]:
        account_obj = self.session.query(AccountOrm). \
            filter(
            AccountOrm.client_id == client_id
        ).all()

        return [Account.parse_obj(obj.__dict__) for obj in account_obj]

    @catch_sqlalchemy_exception
    def update(self, client_id: str, account_id: str, value: float, updated_at: datetime):
        account_obj = self.session.query(AccountOrm). \
            filter(AccountOrm.id == account_id). \
            first()

        if not account_obj:
            raise AccountNotFoundError(client_id, account_id)

        account_obj.balance += Decimal(value)
        account_obj.updated_at = updated_at
        self.session.commit()

    def delete(self, client_id: str) -> None:
        pass
