from typing import Tuple
from src.app.errors.entity_errors import ParamNotValidated


class Transaction:
    account_destiny: str
    value: float
    transaction_type: str

    def __init__(self, account_destiny: str, value: float, transaction_type: str):
        self.account_destiny = account_destiny
        validation_price = self.validate_price(value)
        if validation_price[0] is False:
            raise ParamNotValidated("price", validation_price[1])
        self.value = value
        self.transaction_type = transaction_type

    @staticmethod
    def validate_account_destiny(account_destiny: str) -> Tuple[bool, str]:
        if account_destiny is None:
            return (False, "account is required")
        if type(account_destiny) != str:
            return (False, "account must be a string")
        return (True, "")

    @staticmethod
    def validate_price(price: float) -> Tuple[bool, str]:
        if price is None:
            return (False, "price is required")
        if type(price) != float:
            return (False, "price must be a float")
        if price < 0:
            return (False, "price must be greater than 0")
        return (True, "")

    def to_dict(self):
        return {
            "price": self.price,
            "current_balance": self.current_balance,
            "transaction_type": self.transaction_type
        }
