# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")


def change_direction(speed, x_location, robot_width):
    if speed > 0 and x_location+robot_width >= 640:
        return -speed
    elif speed < 0 and x_location <= 0:
        return -speed
    else:
        return speed

width = robot.get_width()
height = robot.get_height()

#First robot
x1 = 0
y1 = 100
velocity1 = 0.1

#Second robot 
x2 = 0
y2 = 200
velocity2 = 0.2

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))
    window.blit(robot, (x1, y1))
    window.blit(robot, (x2, y2))
    pygame.display.flip()

    x1 += velocity1
    x2 += velocity2
    velocity1 = change_direction(velocity1, x1, width)
    velocity2 = change_direction(velocity2, x2, width)
