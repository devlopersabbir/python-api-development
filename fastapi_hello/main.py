from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {
        "message": "Hello world"
    }

# http://localhost:5000/user


@app.get("/user")
async def user():
    return {
        "id": 1,
        "name": "Sabbir",
        "email": "sabbir@sab.com",
        "password": "sabbir"
    }
