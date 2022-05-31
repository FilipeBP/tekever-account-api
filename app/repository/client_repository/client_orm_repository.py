from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from config import settings
from exception.client_exception import ClientNotFound
from model.client_model import ClientIn, Client, ClientOut
from model.transaction_model import Transaction
from .client_abstract_repository import ClientAbstractRepository
from ..orm_schema import ClientOrm, AccountOrm, TransactionOrm


class ClientOrmRepository(ClientAbstractRepository):
    def __init__(self):
        self.engine = create_engine(
            f'sqlite:///{settings.SQLITE_PATH}'
        )

        self.session = Session(self.engine)

    def create(self, client_info: Client) -> str:
        client = ClientOrm(**client_info.dict())
        self.session.add(client)
        self.session.commit()
        self.session.close()

        return client_info.id

    def get(self, client_id: str) -> ClientOut:
        client_obj = self.session.query(ClientOrm, AccountOrm, TransactionOrm). \
            join(AccountOrm, ClientOrm.id == AccountOrm.client_id, isouter=True). \
            join(TransactionOrm, AccountOrm.id == TransactionOrm.account_id, isouter=True). \
            filter(
                ClientOrm.id == client_id
        ).all()

        if not client_obj:
            raise ClientNotFound(client_id)

        balance = sum(obj[1].balance for obj in client_obj) if client_obj[0][1] else 0.0
        transactions = [Transaction(**obj[2].__dict__) for obj in client_obj] if client_obj[0][2] else []
        return ClientOut(balance=balance, transactions=transactions, **client_obj[0][0].__dict__)

    def update(self, client_id: str, client_info: ClientIn) -> None:
        pass

    def delete(self, client_id: str) -> None:
        pass
