### Most Uses Response Code

- `100` and above are for "Information". You rarely use them directly. Responses with these status codes cannot have a body.
- `200` and above are for "Successful" responses. These are the ones you would use the most.
- `200` is the default status code, which means everything was "OK".
  Another example would be 201, "Created". It is commonly used after creating a new record in the database.
  A special case is 204, "No Content". This response is used when there is no content to return to the client, and so the response must not have a body.
- `300` and above are for "Redirection". Responses with these status codes may or may not have a body, except for 304, "Not Modified", which must not have one.
- `400` and above are for "Client error" responses. These are the second type you would probably use the most.
  An example is 404, for a "Not Found" response.
  For generic errors from the client, you can just use 400.
- `500` and above are for server errors. You almost never use them directly. When something goes wrong at some part in your application code, or server, it will automatically return one of these status codes.
