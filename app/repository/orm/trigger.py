from sqlalchemy import event
from sqlalchemy.orm.attributes import get_history

from model.transaction_model import Transaction
from repository.orm.schema import AccountOrm
from repository.get_repositories import account_repository, transaction_repository


@event.listens_for(account_repository.session, 'after_flush')
def add_transaction_on_insert(session, flush_context):
    new_data = filter(lambda x: isinstance(x, AccountOrm), session.new)

    for obj in new_data:
        transaction_info = Transaction.create_transaction(
            obj.id,
            obj.balance
        )

        transaction_repository.create(transaction_info, external_session=session)


@event.listens_for(AccountOrm, 'before_update')
def add_transaction_on_update(mapper, connection, target):
    balance_history = get_history(target, 'balance')
    transaction_amount = balance_history.added[0] - balance_history.deleted[0]

    transaction_info = Transaction.create_transaction(
        target.id,
        transaction_amount
    )

    transaction_repository.create(transaction_info)
