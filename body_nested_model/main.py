from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from model.user import UserModel

app = FastAPI()


@app.put("/", tags=["update profile"])
async def update_user(request_body: UserModel):
    encoded = jsonable_encoder(request_body)
    print(encoded)
    return JSONResponse(content=encoded, status_code=200)


@app.get("/", tags=["Health"])
async def root_route():
    return {"Hello": "Hello World"}
