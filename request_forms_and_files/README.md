### WARN

You can declare multiple `File` and `Form` parameters in a path operation, but you can't also declare `Body` fields that you expect to receive as JSON, as the request will have the body encoded using `multipart/form-data` instead of `application/json`.

This is not a limitation of FastAPI, it's part of the HTTP protocol.
