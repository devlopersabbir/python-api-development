from typing import Annotated
from fastapi import FastAPI, Path, Query
from fastapi.responses import JSONResponse

app = FastAPI()


@app.get("/products/{product_id}", tags=["Get single product"])
def getProduct(product_id: int):
    print(product_id)
    return {"hello"}


@app.get("/products/{product_id}", tags=["Get single product"])
def getProduct(product_id: int):
    print(product_id)
    return {"hello"}


@app.get("/users/{id}", tags=["get single user"])
async def getUser(id: Annotated[int, Path(title="user id")]):
    print(id)
    result = {
        "id": 1
    }
    if id:
        result.update({"path": id})
    return JSONResponse(content=result, status_code=200)


@app.get("/posts/{id}", tags=["get single post"])
async def get_post(id: Annotated[int, Path(title="post id", ge=0, le=20)], query: Annotated[str | None, Query(alias="your_name")] = None):
    result = {
        "id": 1
    }
    if id and query:
        result.update({"post_id": id, "query": query})
    return JSONResponse(content=result, status_code=200)
