import pytest
from src.app.main import get_client
from src.app.repo.client_repository_mock import ClientRepositoryMock
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
