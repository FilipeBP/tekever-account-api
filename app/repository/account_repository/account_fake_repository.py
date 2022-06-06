from typing import List

from model.account_model import Account
from .account_abstract_repository import AccountAbstractRepository


class AccountFakeRepository(AccountAbstractRepository):
    def create(self, account_info: Account):
        pass

    def get(self, client_id: str, account_id: str) -> Account:
        pass

    def get_by_client(self, client_id: str) -> List[Account]:
        pass

    def update(self, account_id: str, account_info: Account):
        pass

    def delete(self, client_id: str) -> None:
        pass
