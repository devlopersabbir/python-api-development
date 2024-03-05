from fastapi import FastAPI, Body
from typing import Annotated
from datetime import datetime, time, timedelta
from pydantic import BaseModel
from uuid import uuid4

app = FastAPI()


class model(BaseModel):
    uuid: str = uuid4()
    start: datetime | None
    end: datetime | None
    repeat: time | None
    proced: timedelta | None


@app.put("/", tags=["routes"])
def routes(requestModel: Annotated[model, Body()]):
    # print(requestModel)

    start_process = requestModel.start + requestModel.proced
    duration = requestModel.end - start_process

    print(duration)
    pass
