## Extra Data Types

Here are some of the additional data types you can use:

- `UUID:`
  - A standard "Universally Unique Identifier", common as an ID in many databases and systems.
  - In requests and responses will be represented as a `str`.
- `datetime.datetime:`
  - A Python `datetime.datetime`.
  - In requests and responses will be represented as a `str` in ISO 8601 format, like: `2008-09-15T15:53:00+05:00`.
- `datetime.date:`
  - Python `datetime.date`.
  - In requests and responses will be represented as a `str` in ISO 8601 format, like: `2008-09-15`.
- datetime.time:
  - A Python `datetime.time`.
  - In requests and responses will be represented as a `str` in ISO 8601 format, like: `14:23:55.003`.
- `datetime.timedelta:`
  - A Python `datetime.timedelta`.
  - In requests and responses will be represented as a float of total seconds.
  - Pydantic also allows representing it as a "ISO 8601 time diff encoding", see the docs for more info.

### Example model

```py
from typing import Annotated
from datetime import datetime, time, timedelta
from pydantic import BaseModel
from uuid import uuid4

class model(BaseModel):
    uuid: str = uuid4()
    start: datetime | None
    end: datetime | None
    repeat: time | None
    proced: timedelta | None
```
