from fastapi import FastAPI, File, Form, UploadFile
from typing import Annotated

app = FastAPI()

@app.get("/")
async def root():
    return {"hello" : "world"}


@app.post("/")
async def create(
    file: Annotated[bytes, File()],
    fileUpload: Annotated[UploadFile, File()],
    token: Annotated[str, Form()]
    ):
    return {
        "file_size": len(file),
        "token": token,
        "fileb_content_type": fileUpload.content_type,
    }
