from fastapi import FastAPI, status
from enum import Enum
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder

class Tags(Enum):
    items = "items"
    users = "users"
    entry = "entry point"

class Item(BaseModel):
    name: str
    username: str
    password: str

app = FastAPI()
@app.post("/", response_model=Item, status_code=status.HTTP_200_OK, tags=[Tags.entry], response_description="its just response our user", deprecated=True)
async def root(user: Item):
    """
    ## creating a user
    - **name**: user full name
    """
    convert = jsonable_encoder(user)
    return convert
