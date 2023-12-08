from fastapi import FastAPI

app = FastAPI()
fake_items_db:list[dict[str, str]]= [{"item_name": "1"}, {"item_name": "2"}, {"item_name": "3"}]
@app.get("/")
async def index(skip:int = 0, limit:int = 10):
    item = fake_items_db[skip:skip + limit]
    return [item]