from PCA9685_Abstraction.servo_driver import Axis

class EventManager:
    def __init__(self, cam_gimbal, motor_controller, nerf_trigger):
        self.cam_gimbal = cam_gimbal
        self.motor_controller = motor_controller
        self.nerf_trigger = nerf_trigger

    async def process_event(self, event):
        if "axis" in event:
            self._process_axis_event(event)
        elif "button" in event:
            await self._process_button_event(event)

    def _process_axis_event(self, event):
        if event['axis'] in [Axis.RIGHT_JOYSTICK_HORIZONTAL.value, Axis.RIGHT_JOYSTICK_VERTICAL.value]:
            self.cam_gimbal.move(event)
        else:
            self.motor_controller.move(event)

    async def _process_button_event(self, event):
        if event['button'] == 0:
            await self.nerf_trigger.fire()
