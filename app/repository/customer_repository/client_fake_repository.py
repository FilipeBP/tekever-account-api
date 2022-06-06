from model.customer_model import CustomerIn, Customer
from .customer_abstract_repository import CustomerAbstractRepository


class CustomerFakeRepository(CustomerAbstractRepository):
    def create(self, customer_info: CustomerIn):
        pass

    def get(self, customer_id: str) -> Customer:
        pass

    def update(self, customer_id: str, customer_info: CustomerIn):
        pass

    def delete(self, customer_id: str) -> None:
        pass
