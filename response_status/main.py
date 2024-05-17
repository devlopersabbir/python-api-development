from fastapi import FastAPI, status, Response

app = FastAPI()

@app.get("/")
def read_root():
    return Response(content="Hello World", status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)