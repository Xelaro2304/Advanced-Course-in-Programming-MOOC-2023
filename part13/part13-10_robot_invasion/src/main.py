# WRITE YOUR SOLUTION HERE:
import pygame
from random import randint

class Robot:
    def __init__(self, width, height, robot_width, robot_height, velocity):
        self.x = randint(0, width-robot_width)
        self.y = randint(-2*height, 0-robot_height)
        self.velocity = velocity

    def fall(self):
        self.y += self.velocity
    
    def leave(self, direction):
        if direction == 0:
            self.x -= self.velocity
        else:
            self.x += self.velocity

pygame.init()
width, height = 640, 480
window = pygame.display.set_mode((width, height))
robot_image = pygame.image.load("robot.png")
clock = pygame.time.Clock()
 
robot_width = robot_image.get_width()
robot_height = robot_image.get_height()
bottom_of_screen = height - robot_height
half_screen = width/2
right_edge = width - robot_width
velocity = 1 
number_of_robots = 15

robots = []
for i in range(number_of_robots):
    robots.append(Robot(width, height, robot_width, robot_height, velocity))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))
    for robot in robots:
        window.blit(robot_image, (robot.x, robot.y))
    pygame.display.flip()

    robot_number = 0
    for robot in robots:
        
        if robot.y < bottom_of_screen:
            robot.fall()
        elif robot.y >= bottom_of_screen:
            robot.y = bottom_of_screen
            if robot.x+robot_width/2 <= half_screen:
                robot.leave(0)
            else:
                robot.leave(1)
        if robot.y == bottom_of_screen and (robot.x >= width or robot.x < 0-robot_width):
            robots[robot_number] = Robot(width, height, robot_width, robot_height, velocity)
        robot_number += 1



    clock.tick(60)
 