from fastapi import FastAPI, WebSocket
import json
from Controller.Controller import Controller

app = FastAPI()

my_controller = Controller()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        event = json.loads(data)
        my_controller.move(event)
