import pytest
from src.app.main import get_client
from src.app.repo.client_repository_mock import ClientRepositoryMock
from src.app.repo.transaction_repository_mock import TransactionRepositoryMock
from src.app.entities.client import Client

class Test_Main:
    def test_get_client(self):
        repo = ClientRepositoryMock()
        client_account = "12345-5"
        
        client = repo.get_client(client_account)
        
        assert client is not None, "Cliente não encontrado."
        
        expected_client = Client(name="Gabriel", account="12345-5", balance=120.0, agency="1111")
        assert client.name == expected_client.name, f"Nome do cliente esperado: {expected_client.name}, mas foi: {client.name}"
        assert client.account == expected_client.account, f"Conta do cliente esperada: {expected_client.account}, mas foi: {client.account}"
        assert client.balance == expected_client.balance, f"Saldo do cliente esperado: {expected_client.balance}, mas foi: {client.balance}"
        assert client.agency == expected_client.agency, f"Agência do cliente esperada: {expected_client.agency}, mas foi: {client.agency}"

    def test_post_transaction(self):
        repo = TransactionRepositoryMock()
        account_destiny = "22222-3"
        value = 500.0
        transaction_type = "deposit"
        
        new_transaction = repo.post_transaction(account_destiny, value, transaction_type)
        
        assert new_transaction is not None, "Transação não foi criada."
        assert new_transaction.account_destiny == account_destiny, f"Conta de destino esperada: {account_destiny}, mas foi: {new_transaction.account_destiny}"
        assert new_transaction.value == value, f"Valor da transação esperado: {value}, mas foi: {new_transaction.value}"
        assert new_transaction.transaction_type == transaction_type, f"Tipo de transação esperado: {transaction_type}, mas foi: {new_transaction.transaction_type}"
        
        transactions = repo.transactions
        new_id = max(transactions.keys())
        assert new_id in transactions, "Nova transação não foi adicionada ao repositório."
        assert transactions[new_id] == new_transaction, "Transação no repositório não corresponde à transação criada."
