from fastapi import FastAPI, Body
from pydantic import Field, BaseModel
from typing import Annotated

app = FastAPI()

class User(BaseModel):
    name: str | None
    username: str
    bio: str | None = Field(
        title="User bio description",
        max_length=4000
    )
    salary: float = Field(
        ge=1000
    )
    age: int | None = 20


@app.put("/users/{userId}", tags=["update user"])
async def update_user(userId: int, user: Annotated[User, Body(embed=True)]):
    results = {
        "userId": userId,
        "user": user
    }
    print(results)
    return results

@app.get("/", tags=["Health"])
async def read_root():
    return {"message": "Hello World"}