import pygame
import asyncio

class XboxController:
    def __init__(self, input_queue):
        pygame.init()
        self.valid_axis = [0,2,3,4,5]
        self.valid_buttons = [0]
        self.remote_controller = pygame.joystick.Joystick(0)
        self.remote_controller.init()
        self.input_queue = input_queue

    async def monitor_events(self):
        while True:
            await asyncio.sleep(1/60)
            for event in pygame.event.get():
                if event.type == pygame.JOYAXISMOTION and event.axis in self.valid_axis:
                    event_map = {
                        "axis": int(event.axis),
                        "value": float(event.value)
                    }
                    await self.input_queue.put(event_map)
                elif event.type == pygame.JOYBUTTONDOWN and event.button in self.valid_buttons:
                    event_map = {
                        "button": int(event.button),
                        "state": "down"
                    }
                    await self.input_queue.put(event_map)
