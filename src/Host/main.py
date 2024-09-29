from fastapi import FastAPI, WebSocket
import json
from DrivingControl.Controller import DrivingController
from Cam.gimbal import CamGimbal
from PCA9685_Abstraction.servo_driver import Axis

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()
motor_controller = DrivingController()
cam_gimbal = CamGimbal()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        try:
            logger.info(f"received {data}")
            event = json.loads(data)
            if event['axis'] in [Axis.RIGHT_JOYSTICK_HORIZONTAL.value, Axis.RIGHT_JOYSTICK_VERTICAL.value]:
                cam_gimbal.move(event)
            else:
                motor_controller.move(event)
        except Exception as e:
            logger.error(e)
