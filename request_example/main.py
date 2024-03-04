from fastapi import FastAPI, Body
from typing import Annotated
from models.user import UserModel1, UserModel2, UserModel3


app = FastAPI()


@app.get("/", tags=["root route for hello world"])
def root_routes():
    return {"hello": "world"}


@app.put("/1", tags=['update user 1'])
def update_user(request_body: Annotated[UserModel1, Body(example={
    "name": "sabbir"
})]):
    print(request_body)
    pass


@app.put("/2", tags=['update user 2'])
def update_user2(request_body: Annotated[UserModel2, Body()]):
    print(request_body)
    pass


@app.put("/3", tags=['update user 3'])
def update_user3(request_body: Annotated[UserModel3, Body()]):
    print(request_body)
    pass
