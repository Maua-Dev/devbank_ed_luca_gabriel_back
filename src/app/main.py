from fastapi import FastAPI, HTTPException
from mangum import Mangum

from .environments import Environments

from .errors.entity_errors import ParamNotValidated

app = FastAPI()

repo = Environments.get_item_repo()()

@app.get("/")
def get_client():
    return {
        "API": "OK"
    }

@app.post("/deposit")
def post_transaction():
    return {}


handler = Mangum(app, lifespan="off")
