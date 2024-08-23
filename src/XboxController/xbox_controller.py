import pygame
import asyncio

class XboxController:
    def __init__(self, input_queue, my_logger):
        pygame.init()
        self.my_logger = my_logger
        self.joysticks = []
        self.clock = pygame.time.Clock()
        self.valid_axis = [0,4,5]
        self._connect_joysticks()
        self.input_queue = input_queue

    def _connect_joysticks(self):
        for i in range(0, pygame.joystick.get_count()):
            self.joysticks.append(pygame.joystick.Joystick(i))
            self.joysticks[-1].init()
            print ("Detected joystick "),self.joysticks[-1].get_name(),"'"

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
