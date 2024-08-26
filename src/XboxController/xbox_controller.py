import pygame
import asyncio

class XboxController:
    def __init__(self):
        pygame.init()
        self.valid_axis = [0,4,5]
        self.remote_controller = pygame.joystick.Joystick(0)
        self.remote_controller.init()

    async def get_event(self):
        event = pygame.event.poll()
        if event.type == pygame.JOYAXISMOTION and event.axis in self.valid_axis:
            event_map = {
                "axis": int(event.axis),
                "value": float(event.value)
            }
            return event_map
        return None
