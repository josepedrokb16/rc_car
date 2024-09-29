import pygame

pygame.init()
remote_controller = pygame.joystick.Joystick(0)
remote_controller.init()

while True:
    event = pygame.event.poll()
    if event.type == pygame.JOYAXISMOTION and event.axis == 5:
        print(event)
