import pytest
from src.app.main import get_client
from src.app.repo.client_repository_mock import ClientRepositoryMock


class Test_Main:
    def test_get_client(self):
        repo = ClientRepositoryMock()
        client_account = "12345-5"
        repo.get_client(client_account)