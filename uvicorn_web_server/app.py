async def app(scope, receive, send):
    assert scope["type"] == "http"

    try:
        await send({
            "type": "http.response.start",
            "status": 200,
            "headers": [
                [b"content-type", b"text-plain"]
            ]
        })
        await send({
            "type": "http.response.body",
            "body": b'<div><h1>hello h1</h1><h2>hello h2</h2></div>'
        })
    except:
        print("Fail to start server!")
