from aiohttp import web
import json


USERS = set()

def event_msg(message):
    return json.dumps({"action": "message", "value": message})

def register(websocket):
    USES.add(websocket)

def unregister(websocket):
    USES.remove(websocket)

async def notify_all(message):
    await asyncio.wait([user.send_str(message) for user in USER])

async def notify(message, websocket):
    await websocket.send_str(message)

async def join_group(request):
    websocket = aiohttp.web.WebSocketResponse()
    await websocket.prepare(request)
    await register(websocket)
    try:
        async for msg in websocket:
            data = json.loads(msg.data)
            if data["action"] == "message":
                print(data["value"])
                await notify_all(eventmsg(datta["value"]))
            else:
                print("unsupported event: {%s}" % data)
    finally:
        await unregister(websocket)


async def connect(request):
    websocket = aiohttp.web.WebSocketResponse()
    await websocket.prepare(request)
    try:
        async for msg in websocket:
            data = json.loads(msg.data)
            if data["action"] == "message":
                print(data["value"])
                await notify(eventmsg(datta["value"]), websocket)
            else:
                print("unsupported event: {%s}" % data)

app = web.Application()
app.add_routes([web.get('/ws/group', join_group)])
app.add_routes([web.get('/ws', connect)])

if __name__ == '__main__':
    web.run_app(app, host="0.0.0.0", port=8080)
