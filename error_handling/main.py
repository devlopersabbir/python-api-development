from fastapi import FastAPI, HTTPException

app = FastAPI()

items = {"food": "The food says, hi"}

@app.get("/items/{query}", tags=["GET single ID"])
async def read_items(query: str):
    if query not in items:
        raise HTTPException(status_code=404, detail="Item not found", headers={"X-Error": "There go my error"})
    return {"item": items[query]}