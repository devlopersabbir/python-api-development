async def app(scope, receive, send):
    assert scope["type"] == "http"

    try:
        await send({
            "type": 'http.response.start',
            "status": 200,
            "header": [
                [b"content-type", b"text-plain"],
            ]
        })
        await send({
            "type": "http.response.body",
            "body": b"<h1>Hello World</h1>"
        })
    except:
        print("Fail to run server")
