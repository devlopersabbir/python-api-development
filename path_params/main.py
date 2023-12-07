from enum import Enum
from fastapi import FastAPI, status
from fastapi.responses import JSONResponse

app = FastAPI()

class Role(str, Enum):
    ADMIN = "ADMIN"
    USER = "USER"

@app.get("/user/{role}")
async def user(role:Role):
    if role is role.ADMIN:
        return JSONResponse(status_code=200, content={
            "message":"You are a admin"
        })
    else:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={
            "message":"Sorry you are not admin!"
        })
    

@app.get("/")
async def health():
    return {
        "message": "Hello"
    }