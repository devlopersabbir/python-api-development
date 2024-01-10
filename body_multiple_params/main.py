from fastapi import FastAPI, Path, Query
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from typing import Annotated

app = FastAPI()

class User(BaseModel):
  name: str | None = None
  username: str
  password: str
  age: int | None = 20

@app.put("/{id}", tags=["update user"])
async def update_user(
  id: Annotated[int, Path(title="user id", le=100, ge=0)],
  query: Annotated[str | None, Query(title="search query")] = None,
  user: User | None = None):
  
  result = {"user_id": id}
  if query:
    result.update({"query": query})
  if user:
    result.update({
      "user": jsonable_encoder(user)
    })
  return JSONResponse(content=result, status_code=200)

@app.get("/")
async def root_route():
  return {"hello": "world"}