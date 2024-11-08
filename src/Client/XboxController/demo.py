import pygame

pygame.init()
remote_controller = pygame.joystick.Joystick(0)
remote_controller.init()

while True:
    event = pygame.event.poll()
    if event.type == pygame.JOYBUTTONDOWN and event.button == 0:
        print(event)
