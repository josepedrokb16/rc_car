import asyncio
import websockets

async def connect():
    uri = "ws://192.168.2.41:8000/ws"
    async with websockets.connect(uri, ping_interval=20, ping_timeout=20) as websocket:
        while True:
            await websocket.send(input("Enter message: "))
            response = await websocket.recv()
            print(response)


asyncio.run(connect())
