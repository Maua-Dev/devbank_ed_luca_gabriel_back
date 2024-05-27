from typing import Tuple
from src.app.errors.entity_errors import ParamNotValidated
from src.app.enums.transaction_type_enum import TransactionTypeEnum

class Transaction:
    account: str
    value: float
    transaction_type: TransactionTypeEnum

    def __init__ (self, value: float, transaction_type: TransactionTypeEnum):
        validation_price = self.validate_price(value)
        if validation_price[0] is False:
            raise ParamNotValidated("price", validation_price[1])
        self.value = value

        validation_transaction_type = self.validate_transaction_type(transaction_type)
        if validation_transaction_type[0] is False:
            raise ParamNotValidated("transaction_type", validation_transaction_type[1])
        self.transaction_type = transaction_type
    
    @staticmethod
    def validate_price(price: float) -> Tuple[bool, str]:
        if price is None:
            return (False, "price is required")
        if type(price) != float:
            return (False, "price must be a float")
        if price < 0:
            return (False, "price must be greater than 0")
        return (True, "")
    
    @staticmethod
    def validate_transaction_type(transaction_type: TransactionTypeEnum) -> Tuple[bool, str]:
        if transaction_type is None:
            return (False, "transaction_type is required")
        if type(transaction_type) != TransactionTypeEnum:
            return (False, "transaction_type must exist in TransactionTypeEnum")
        return (True, "")
    
    def to_dict(self):
        return {
            "price": self.price,
            "current_balance": self.current_balance,
            "transaction_type": self.transaction_type
        }
