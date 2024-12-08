from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel


app = FastAPI()

class User(BaseModel):
    name: str

@app.post("/")
async def root(user: User):
    print(user)
    return JSONResponse(content=jsonable_encoder(user))
