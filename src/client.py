import asyncio
import websockets
import json
from XboxController.xbox_controller import XboxController

class Client:
    def __init__(self):
        self.xbox_controller = XboxController()

    async def connect(self):
        uri = "ws://192.168.2.41:8000/ws"
        async with websockets.connect(uri, ping_interval=20, ping_timeout=20) as websocket:
            while True:
                event = await self.xbox_controller.get_event()
                if event:
                    print(f"sent {event}")
                    await websocket.send(json.dumps(event))

if __name__ == "__main__":
    client = Client()
    asyncio.run(client.connect())
