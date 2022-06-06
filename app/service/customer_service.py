from model.customer_model import Customer
from repository import customer_repository


def get_customer(customer_id):
    return customer_repository.get(customer_id)


def create_customer(client_info):
    customer = Customer.create_customer(client_info)
    customer_id = customer_repository.create(customer)

    return {'detail': 'Customer created', 'id': customer_id}
