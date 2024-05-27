from typing import Dict

from src.app.entities.transaction import Transaction
from src.app.repo.transaction_repository_interface import ITransactionRepository


class TransactionRepositoryMock(ITransactionRepository):
    transactions: Dict[int, Transaction]

    def __init__(self):
        self.transactions = {
            1: Transaction(account_destiny="12345-5", value=120.0, transaction_type="deposit"),
            2: Transaction(account_destiny="11111-2", value=10.0, transaction_type="withdraw"),
            3: Transaction(account_destiny="81638-1", value=0.0, transaction_type="deposit"),
            4: Transaction(account_destiny="91739-9", value=2310.0, transaction_type="withdraw"),
            5: Transaction(account_destiny="91783-6", value=12393.0, transaction_type="deposit")
        }

    def post_transaction(self, account_destiny: str, value: float, transaction_type: str) -> Transaction:
        new_transaction = Transaction(account_destiny, value, transaction_type)
        new_id = max(self.transactions.keys()) + 1
        self.transactions[new_id] = new_transaction
        return new_transaction
