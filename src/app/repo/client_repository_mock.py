from typing import Dict, List, Optional
from .client_repository_interface import IClientRepository
from ..entities.client import Client

class ClientRepositoryMock(IClientRepository):
    clients: Dict[int, Client]

    def __init__(self):
        self.clients = {
            1: Client(name="Gabriel", account="12345-5", balance=120.0, agency="1111"),
            2: Client(name="Luca", account="11111-2", balance=10.0, agency="1212"),
            3: Client(name="Edgar", account="81638-1", balance=0.0, agency="1812"),
            4: Client(name="Rodrigo", account="91739-9", balance=2310.0, agency="8233"),
            5: Client(name="Yuri", account="91783-6", balance=12393.0, agency="8293")
        }

    
    def get_all_client(self) -> List[Client]:
        return self.clients.values()

    def get_client(self, account: str) -> Optional[Client]:
        for client in self.clients.values():
            if client.account == account:
                return client
        return None
    
    def create_client(self, client: Client, id: int) -> Client:
        self.clients[id] = client
        return client

    def update_client(self, id: int, name: str = None, account: str = None, balance: float = None, agency: str = None) -> Client:
        client = self.clients.get(id, None)
        if client is None:
            return None
        
        if name is not None:
            client.name = name
        if account is not None:
            client.account = account
        if balance is not None:
            client.balance = balance
        if agency is not None:
            client.agency = agency
        self.clients[id] = client

        return client
    
    def delete_client(self, id: int) -> Client:
        client = self.clients.pop(id)
        return client