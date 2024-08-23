from fastapi import FastAPI, WebSocket
import json
from Controller.Controller import Controller
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger('uvicorn')

app = FastAPI()

my_controller = Controller()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()  # Accept the WebSocket connection
    while True:
        data = await websocket.receive_text()  # Receive data from the client
        try:
            event = json.loads(data)
            my_controller.move(event)
        except Exception as e:
            logger.info(e)
