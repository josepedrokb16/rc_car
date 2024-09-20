from fastapi import FastAPI, WebSocket
import json
from Controller.MotorController import MotorController
from Cam.cam_gimbal import CamGimbal

import logging
# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()
motor_controller = MotorController()
cam_gimbal = CamGimbal()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        try:
            logger.info(f"received {data}")
            event = json.loads(data)
            if event['axis'] in [2,3]:
                cam_gimbal.move(event)
            else:
                motor_controller.move(event)
        except Exception as e:
            logger.error(e)
