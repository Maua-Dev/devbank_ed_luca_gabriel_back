from typing import Tuple
from ..errors.entity_errors import ParamNotValidated

class Client:
    name: str
    account: str
    balance: float
    agency: str

    def __init__(self, name: str, account: str, balance: float, agency: str):
        validation_name = self.validate_name(name)
        if validation_name[0] is False:
            raise ParamNotValidated("name", validation_name[1])
        self.name = name

        validation_account = self.validate_account(account)
        if validation_account[0] is False:
            raise ParamNotValidated("account", validation_account[1])
        self.account = account

        validation_balance = self.validate_balance(balance)
        if validation_balance[0] is False:
            raise ParamNotValidated("balance", validation_balance[1])
        self.balance = balance

        validation_agency = self.validate_agency(agency)
        if validation_agency[0] is False:
            raise ParamNotValidated("agency", validation_agency[1])
        self.agency = agency
    
    @staticmethod
    def validate_name(name: str) -> Tuple[bool, str]:
        if name is None:
            return (False, "Name is required")
        if type(name) != str:
            return (False, "Name must be a string")
        if len(name) < 3:
            return (False, "Name must be at least 3 characters long")
        return (True, "")
    
    @staticmethod
    def validate_account(account: str) -> Tuple[bool, str]:
        if account is None:
            return (False, "Account is required")
        if type(account) != str:
            return (False, "Account must be a string")
        if len(account) < 7 and account[5] != '-':
            return (False, "The account must be type XXXXX-X")
        return (True, "")
    
    @staticmethod
    def validate_balance(balance: float) -> Tuple[bool, str]:
        if balance is None:
            return (False, "Baland is Required")
        if type(balance) != float:
            return (False, "Balande must be a float")
        return (True, "")
    
    @staticmethod
    def validate_agency(agency: str) -> Tuple[bool, str]:
        if agency is None:
            return (False, "Agency is required")
        if type(agency) != str:
            return (False, "Agency must be a string")
        if len(agency) != 4:
            return (False, "Agency must be made up of 4 digits")
        return (True, "")
    
    def to_dict(self):
        return {
            "name": self.name,
            "account": self.account,
            "balance": self.balance,
            "agency": self.agency
        }
