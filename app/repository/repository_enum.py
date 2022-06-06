from enum import Enum, auto


class CustomerRepositoryEnum(str, Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name.lower()

    ORM = auto()
    FAKE = auto()


class AccountRepositoryEnum(str, Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name.lower()

    ORM = auto()
    FAKE = auto()


class TransactionRepositoryEnum(str, Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name.lower()

    ORM = auto()
    FAKE = auto()