from fastapi import FastAPI, HTTPException, Query
from mangum import Mangum
from repo.client_repository_interface import IClientRepository
from src.app.repo.transaction_repository_interface import ITransactionRepository
from .environments import Environments
from .errors.entity_errors import ParamNotValidated

app = FastAPI()


class MyApp:
    def __init__(self, client_repository: IClientRepository, transaction_repository: ITransactionRepository):
        self.client_repository = client_repository
        self.transaction_repository = transaction_repository


repo = Environments.get_item_repo()()
my_app = MyApp(repo)


@app.get("/")
def get_client(self, account: str):
    try:
        client = self.client_repository.get_client(account)
        if client is None:
            raise HTTPException(status_code=404, detail="Client not found")
        return client
    except ParamNotValidated as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/deposit")
def post_transaction(self, account: str, value: float, transaction_type: str = Query(None)):
    try:
        self.transaction_repository.post_transaction(
            account, value, transaction_type)
    except ParamNotValidated as e:
        raise HTTPException(status_code=400, detail=str(e))


handler = Mangum(app, lifespan="off")
