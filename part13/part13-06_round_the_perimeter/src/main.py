# # WRITE YOUR SOLUTION HERE:
import pygame
pygame.init()

window_width = 640
window_height = 480

window = pygame.display.set_mode((window_width, window_height))
robot = pygame.image.load("robot.png")

width = robot.get_width()
height = robot.get_height()

x = 0
y = 0
velocity = 1
direction = 'right'

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    pygame.display.flip()


    if direction == 'right':                               
        x += velocity
        if x + width >= window_width: 
            x = window_width - width   
            direction = 'down'                              
    elif direction == 'down':                               
        y += velocity
        if y + height >= window_height:
            y = window_height - height
            direction = 'left'                              
    elif direction == 'left':                              
        x -= velocity
        if x <= 0:                                 
            direction = 'up'
    elif direction == 'up':                               
        y -= velocity
        if y <= 0:                               
            direction = 'right'

    clock.tick(60)
