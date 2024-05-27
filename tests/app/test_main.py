import pytest
from src.app.main import get_client
from src.app.repo.client_repository_mock import ClientRepositoryMock


class Test_Main:
    def test_get_client(self):
        repo = ClientRepositoryMock()
        client_account = "12345-5"
        response = get_client(self, account=client_account)
        assert response == {
            'account': client_account,
            'client': repo.clients.get(client_account).to_dict()
        }
