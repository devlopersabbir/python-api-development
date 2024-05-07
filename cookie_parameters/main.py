from fastapi import FastAPI, Cookie, Response
from typing import Annotated


app = FastAPI()

@app.get("/")
async def room_routes():
    return {"message": "hello world"}


@app.get("/token", tags=["token"])
async def write_token():
    response = Response(content="cookie is set successfully")
    response.set_cookie(key="token", value="fake-cookie-token", httponly=True, max_age=5,  path="/", secure=False, samesite="strict")
    return response

@app.get("/items", tags=["items"])
async def read_items(token: Annotated[str | None, Cookie()] = None):
    print(token)
    return {"message": "hello items"}