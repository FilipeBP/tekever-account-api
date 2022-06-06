from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from config import settings
from exception.customer_exception import CustomerNotFoundError
from model.customer_model import CustomerIn, Customer, CustomerOut
from model.transaction_model import Transaction
from .customer_abstract_repository import CustomerAbstractRepository
from repository.orm.schema import CustomerOrm, AccountOrm, TransactionOrm


class CustomerOrmRepository(CustomerAbstractRepository):
    def __init__(self):
        self.engine = create_engine(
            f'sqlite:///{settings.SQLITE_PATH}'
        )

        self.session = Session(self.engine)

    def create(self, customer_info: Customer) -> str:
        customer = CustomerOrm(**customer_info.dict())
        self.session.add(customer)
        self.session.commit()
        self.session.close()

        return customer_info.id

    def get(self, customer_id: str) -> CustomerOut:
        customer_obj = self.session.query(CustomerOrm, AccountOrm, TransactionOrm). \
            join(AccountOrm, CustomerOrm.id == AccountOrm.customer_id, isouter=True). \
            join(TransactionOrm, AccountOrm.id == TransactionOrm.account_id, isouter=True). \
            filter(
            CustomerOrm.id == customer_id
        ).all()

        if not customer_obj:
            raise CustomerNotFoundError(customer_id)

        balance = sum(obj[1].balance for obj in customer_obj) if customer_obj[0][1] else 0.0
        transactions = [Transaction(**obj[2].__dict__) for obj in customer_obj] if customer_obj[0][2] else []
        return CustomerOut(balance=balance, transactions=transactions, **customer_obj[0][0].__dict__)

    def update(self, customer_id: str, customer_info: CustomerIn) -> None:
        pass

    def delete(self, customer_id: str) -> None:
        pass
