import asyncio
import websockets
import json
from XboxController.xbox_controller import XboxController

class Client:
    def __init__(self):
        self.input_queue = asyncio.Queue(maxsize=1)
        self.xbox_controller = XboxController(self.input_queue)

    async def connect(self):
        uri = "ws://your-url:8000/ws"
        async with websockets.connect(uri, ping_interval=20, ping_timeout=20) as websocket:
            asyncio.create_task(self.xbox_controller.monitor_events())
            while True:
                state = await self.input_queue.get()
                await websocket.send(json.dumps(state))

if __name__ == "__main__":
    client = Client()
    asyncio.run(client.connect())
