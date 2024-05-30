from fastapi import FastAPI, Form
from fastapi import Request
from typing import Annotated

app = FastAPI()

@app.get("/")
def read_root(username: Annotated[str, Form()], password: Annotated[str, Form()]):
    print(username)
    print(password)
    return {"Hello": "World"}


@app.post("/")
async def read_root(request: Request):
    form = await request.form()
    formData = dict(form)

    print(formData["name"])
    return {"Hello": "World"}