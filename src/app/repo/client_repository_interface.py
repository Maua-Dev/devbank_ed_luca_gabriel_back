from abc import ABC, abstractmethod
from src.app.entities.client import Client

class IClientRepository(ABC):

    @abstractmethod
    def get_all_client(self):
        pass

    @abstractmethod
    def get_client(self, account: float):
        pass

    @abstractmethod
    def create_client(self, client: Client):
        pass

    @abstractmethod
    def update_client(self, id: int, name: str=None, account: str=None, balance: float=None, agency: str=None):
        pass
    
    @abstractmethod
    def delete_client(self, id: int):
        pass