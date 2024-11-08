from fastapi import FastAPI, WebSocket
import json
from DrivingControl.Controller import DrivingController
from Cam.gimbal import CamGimbal
from EventManager.event_manager import EventManager
from Nerf.trigger import Trigger

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()
motor_controller = DrivingController()
cam_gimbal = CamGimbal()
trigger = Trigger()
event_manager = EventManager(cam_gimbal, motor_controller, trigger)

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        try:
            logger.info(f"received {data}")
            event = json.loads(data)
            await event_manager.process_event(event)
        except Exception as e:
            logger.error(e)
