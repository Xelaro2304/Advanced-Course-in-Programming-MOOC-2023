# WRITE YOUR SOLUTION HERE:
import pygame
import random

pygame.init()
window_width = 640
window_height = 480
window = pygame.display.set_mode((window_width, window_height))

robot = pygame.image.load("robot.png")
robot_width = robot.get_width()
robot_height = robot.get_height()

window.fill((0, 0, 0))

for i in range(1000):
    width = random.randint(0,window_width-robot_width)
    height = random.randint(0,window_height-robot_height)
    window.blit(robot, (width, height))

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()