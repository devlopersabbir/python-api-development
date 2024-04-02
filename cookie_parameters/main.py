from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def room_routes():
    return {"message": "hello world"}