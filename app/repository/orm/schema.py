from sqlalchemy import Column, String, Numeric, ForeignKey, DateTime, Integer, event, CheckConstraint
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class ClientOrm(Base):
    __tablename__ = 'clients'

    id = Column(String, primary_key=True)
    name = Column(String(20), nullable=False)
    surname = Column(String(40))

    accounts = relationship('AccountOrm', back_populates='client')


class AccountOrm(Base):
    __tablename__ = 'accounts'

    id = Column(String, primary_key=True)
    client_id = Column(String, ForeignKey('clients.id'), index=True)
    balance = Column(Numeric(10, 2), nullable=False)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    client = relationship('ClientOrm', back_populates='accounts')
    transactions = relationship('TransactionOrm', back_populates='account')

    __table_args__ = (
        (CheckConstraint('balance >= 0'), )
    )


class TransactionOrm(Base):
    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True)
    account_id = Column(String, ForeignKey('accounts.id'), index=True)
    amount = Column(Numeric(10, 2), nullable=False)
    created_at = Column(DateTime)

    account = relationship('AccountOrm', back_populates='transactions')

