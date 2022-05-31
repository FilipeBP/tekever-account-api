from model.client_model import Client
from repository import client_repository


def get_client(client_id):
    return client_repository.get(client_id)


def create_client(client_info):
    client = Client.create_client(client_info)
    client_id = client_repository.create(client)

    return {'detail': 'Client created', 'id': client_id}
