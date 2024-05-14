from fastapi import FastAPI, Request, Header
from typing import Annotated

app = FastAPI()

@app.get("/", tags=["Health"])
def root():
    return {"message": "hello world"}


# @app.get("/header")
# def header_params(req: Request):
#     headers = dict(req.headers)
#     print(headers)
#     return "hello"


@app.get("/header")
def header_params(user_agent: Annotated[str | None, Header()] = None):
    print(user_agent)
    return "hello"