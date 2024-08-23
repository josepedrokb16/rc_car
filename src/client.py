import asyncio
import websockets
import json
from XboxController.xbox_controller import XboxController
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger('my_logger')

class Client:
    def __init__(self, logger):
        self.input_queue = asyncio.Queue()
        self.xbox_controller = XboxController(self.input_queue, logger)
        self.my_logger = logger

    async def send_heartbeat(self, websocket):
        while True:
            await websocket.send("ping")
            await asyncio.sleep(10)  # Send a heartbeat every 30 seconds

    async def connect(self):
        uri = "ws://192.168.2.41:8000/ws"
        async with websockets.connect(uri, ping_interval=20, ping_timeout=20) as websocket:
            asyncio.create_task(self.send_heartbeat(websocket))
            asyncio.create_task(self.xbox_controller.monitor_events())

            while True:
                state = await self.input_queue.get()
                self.my_logger.info(f"got state from queue: {state}")
                # state = input("type: ")
                await websocket.send(json.dumps(state))
                response = await websocket.recv()
                print(f"Received: {response}")

if __name__ == "__main__":
    client = Client(logger)
    asyncio.run(client.connect())
