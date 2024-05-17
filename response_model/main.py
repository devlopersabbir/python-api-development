from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from models.User import User

app = FastAPI()

db: list[User] = []

@app.get("/new")
def new():
    return {"message": "This is the redirect page!"}

@app.get("/", response_model=list[User])
def read()-> list[User]:
    isEmpty = len(db) == 0
    if isEmpty:
        return RedirectResponse("/new", status_code=302)
    return db

@app.post("/")
def create(user: User):
    db.append(user)
    return {"message": "User has been created successfully!", "user": user.dict()}