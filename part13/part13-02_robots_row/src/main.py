# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")
width = robot.get_width()
height = robot.get_height()
initial_width = 30
initial_height = 80

window.fill((0, 0, 0))

for i in range(10):
    window.blit(robot, (initial_width, initial_height))
    initial_width += 50

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()