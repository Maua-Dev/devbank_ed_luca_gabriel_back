from abc import ABC, abstractmethod
from src.app.entities.client import Client

class ITransactionRepository(ABC):

    @abstractmethod
    def post_transaction(self, account: str, value: float, transaction_type: str):
        pass