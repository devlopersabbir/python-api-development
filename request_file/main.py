from fastapi import FastAPI, File, UploadFile
from typing import Annotated
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/")
async def main():
    content = """
<body>
<form action="/files/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
<form action="/uploadfiles/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
</body>
    """
    return HTMLResponse(content=content)

@app.post("/file")
def read_root(file: Annotated[bytes, File()]):
    print(file.type)
    return {"message": "file uploaded"}

@app.post("/uploadfile")
async def create_upload_file(file: UploadFile):
    if file.content_type != "image/jpeg" and file.content_type != "image/jpg" and file.content_type != "image/png":
        return {"error": "Only image files are allowed"}

    """First way to save the file"""
    with open(file.filename, "wb") as f:
        f.write(file.file.read())

    """Second way to save the file"""
    filePath = file.filename
    fileContent = file.read()

    f = open(filePath, "wb")

    try:
        f.write(fileContent)
    except Exception as e:
        print(e)
    finally:
        f.close()
    return {"filename": "uploaded"}

@app.post("/multiplefiles")
async def create_multiple_files(files: list[UploadFile]):
    print(files)
    return {"filename": "uploaded"}