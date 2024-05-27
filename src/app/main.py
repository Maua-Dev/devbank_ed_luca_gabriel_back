from fastapi import FastAPI, HTTPException, Query
from mangum import Mangum
from src.app.repo.client_repository_interface import IClientRepository
from src.app.repo.transaction_repository_interface import ITransactionRepository
from src.app.environments import Environments
from src.app.errors.entity_errors import ParamNotValidated

app = FastAPI()


class MyApp:
    def __init__(self, client_repository: IClientRepository, transaction_repository: ITransactionRepository):
        self.client_repository = client_repository
        self.transaction_repository = transaction_repository


# Inicializar os repositórios
client_repo = Environments.get_client_repo()()
transaction_repo = Environments.post_transaction_repo()()
my_app = MyApp(client_repo, transaction_repo)


@app.get("/client")
def get_client(account: str):
    try:
        client = my_app.client_repository.get_client_by_account(account)
        if client is None:
            raise HTTPException(status_code=204, detail="Client not found")
        return client
    except ParamNotValidated as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/deposit")
def post_transaction(account: str, value: float, transaction_type: str = Query(None)):
    try:
        my_app.transaction_repository.post_transaction(
            account, value, transaction_type)
        return {"status": "success"}
    except ParamNotValidated as e:
        raise HTTPException(status_code=400, detail=str(e))


handler = Mangum(app, lifespan="off")
