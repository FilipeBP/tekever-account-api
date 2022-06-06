from abc import ABC, abstractmethod

from model.customer_model import CustomerIn, Customer


class CustomerAbstractRepository(ABC):

    @abstractmethod
    def create(self, customer_info: CustomerIn):
        raise NotImplementedError

    @abstractmethod
    def get(self, customer_id: str) -> Customer:
        raise NotImplementedError

    @abstractmethod
    def update(self, customer_id: str, customer_info: CustomerIn):
        raise NotImplementedError

    @abstractmethod
    def delete(self, customer_id: str) -> None:
        raise NotImplementedError
