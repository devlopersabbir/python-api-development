from fastapi import FastAPI, Query
from typing import Annotated

app = FastAPI()

fake_data: dict[str, list[dict[int, str]]] = {
    "items": [
        {1: "Apple"},
        {2: "Banana"}
    ]
}


# @app.get("/items", tags=["Items"])
# async def get_item(q: str | None = None):
#     print(q)
#     return {"hello": "world"}

@app.get("/items", tags=["Items"])
async def get_item(query: Annotated[str, Query(title="Get All Item", description="item get description", alias="sabbir-hossain", deprecated=False)] = None):
    print(query)
    if query:
        fake_data.update({"query": query})
    return fake_data


@app.get("/", tags=["Helth"])
async def helth():
    return {"hello": "world"}
