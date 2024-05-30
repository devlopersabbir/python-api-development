from fastapi import FastAPI, Form
from typing import Annotated

app = FastAPI()

@app.get("/")
def read_root(username: Annotated[str, Form()], password: Annotated[str, Form()]):
    print(username)
    print(password)
    return {"Hello": "World"}