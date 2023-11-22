## Personal Notes

#### What is REST?

**REST Stand for Representational State Transfer** An architectural style for
designing networked applications based on a set of principles, such as stateless
communication and resource-based interactions.

#### What is API

**Application Programming Interface** A set of rules that allows one software
application to interact with another, enabling them to exchange data and
functionality.

#### What is REST API?

**REST API (Representational State Transfer Application Programming
Interface):** An API that adheres to the principles of REST, using standard HTTP
methods (GET, POST, PUT, DELETE) for communication and manipulating resources,
typically exchanging data in a format like JSON.

example about REST API

```plaintext
1. REST: Architectural style for networked apps.
2. API: Rules for software interaction.
3. REST API: Adheres to REST principles, uses HTTP methods. E.g., fetching data with HTTP GET.
```

```console
http://ex.com/api/v1/products
http://ex.com/api -> endpoint
```

1. Benefits of REST API
2. Communication
   - RESTful
   - List of benefit
     - Simple & Standard
     - Scalable & Stateless
     - Performance & Cache

#### How API works in real life

- Talking about (req, res)

#### Request

- Talking about CRUD
  - HTTP method
    - GET | POST | PUT | DELETE/PATCH
  - Request Header
    - Content Type
    - Bearer Token etc
  - Request Body
    ```json
    {
      "id": 0,
      "name": "cup ice",
      "description": "Describe something about cup ice",
      "price": 20
    }
    ```
  - Request Params
    - `http://example.com/?search=cup`

#### Response

- Status
  - 400
    > wrong in client
  - 500
    > wrong in server
  - 200
    > okay
  - 201
    > created

#### Response data & JSON

```json
[
  {
    "id": 0,
    "name": "cup ice",
    "description": "Describe something about cup ice",
    "price": 20
  },
  {
    "id": 1,
    "name": "ice loly",
    "description": "Describe something about cup ice",
    "price": 5
  }
]
```
