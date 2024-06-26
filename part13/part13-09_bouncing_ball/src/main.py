# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()

window_width, window_height = 640, 480

window = pygame.display.set_mode((window_width, window_height))
ball = pygame.image.load("ball.png")

width = ball.get_width()
height = ball.get_height()

h = 1
x = 320
y = 240

xvelocity = 3
yvelocity = 3
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))    
    window.blit(ball, (x, y))
    pygame.display.flip()

    if x+width >= 640 or x <= 0:
        xvelocity = -xvelocity
    if y+height >= 480 or y <= 0:
        yvelocity = -yvelocity

    x += xvelocity
    y += yvelocity

    clock.tick(60)