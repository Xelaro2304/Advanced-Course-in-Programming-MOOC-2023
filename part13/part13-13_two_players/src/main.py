# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")
x = 640 - robot.get_width() - 80
y = 480 - robot.get_height() - 80

x2 = 80
y2 = 80

right1 = False
left1 = False
up1 = False
down1 = False

up2 = False
down2 = False
left2 = False
right2 = False

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                left1 = True
            if event.key == pygame.K_RIGHT:
                right1 = True
            if event.key == pygame.K_UP:
                up1 = True
            if event.key == pygame.K_DOWN:
                down1 = True
            if event.key == pygame.K_a:
                left2 = True
            if event.key == pygame.K_d:
                right2 = True
            if event.key == pygame.K_w:
                up2 = True
            if event.key == pygame.K_s:
                down2 = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                left1 = False
            if event.key == pygame.K_RIGHT:
                right1 = False
            if event.key == pygame.K_UP:
                up1 = False
            if event.key == pygame.K_DOWN:
                down1 = False
            if event.key == pygame.K_a:
                left2 = False
            if event.key == pygame.K_d:
                right2 = False
            if event.key == pygame.K_w:
                up2 = False
            if event.key == pygame.K_s:
                down2 = False

        if event.type == pygame.QUIT:
            exit()

    if right1 and x <= 640 - robot.get_width():
        x += 2
    if left1 and x >= 0:
        x -= 2
    if up1 and y >= 0:
        y -= 2
    if down1 and y <= 480 - robot.get_height():
        y += 2

    if right2 and x2 <= 640 - robot.get_width():
        x2 += 2
    if left2 and x2 >= 0:
        x2 -= 2
    if up2 and y2 >= 0:
        y2 -= 2
    if down2 and y2 <= 480 - robot.get_height():
        y2 += 2

    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    window.blit(robot, (x2, y2))
    pygame.display.flip()

    clock.tick(60)