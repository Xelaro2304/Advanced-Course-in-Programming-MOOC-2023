# In this game, the player controls a robot with the arrow keys and needs to collect coins while avoiding monster
# The monsters appear every 3 seconds on the screen and automatically follow the robot
# Each time a coin is obtained, a new one generates
# If the robot catches the plager, game is over
# Code is not very well optimized and has very much space for improvement by crating classes for the robot and coins, to make code
# more readable but was unable to do it due to time constraints, game is playable, although on game over it freezes and needs to be
# closed by task manager
import pygame
from random import randint

class Monster:
    def __init__(self, width, height):
        self.width = width
        self.height = height

#Creates monsters
    def appear(self, window_width, window_height):
        while True:
            self.x = randint(-0.5*window_width, window_width *1.5)
            self.y = randint(-0.5*window_height, window_height *1.5)
            if (self.x < 0 or self.x > window_width) and (self.y < 0 or self.y > window_height):
                break

#Checks if the monster has trapped the robot
    def catch(self, x, y):
        capture_range = 20
        if self.x in [x+i for i in range (-capture_range,capture_range,1)] and self.y in [y+j for j in range (-capture_range,capture_range,1)]:
            return True
        return False

#Makes the monster follow the robot
    def pursue(self, x, y):
        if self.x < x:
            self.x += 1
        if self.x > x:
            self.x -= 1
        if self.y < y:
            self.y += 1
        if self.y > y:
            self.y -= 1

#Function that checks if the robot has grabbed a coin
def get_coin(robot_x, robot_y, robot_half_width, robot_half_height, x_coin, y_coin):
    capture_range = 30
    if robot_x + robot_half_width in [x_coin+i for i in range (-capture_range,capture_range,1)] and robot_y + robot_half_height in [y_coin+j for j in range (-capture_range,capture_range,1)]:
        return True
    return False

 #Screen configurations 
pygame.init()
window_width = 640
window_height = 480
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Coin chaser")

#Load the images
robot = pygame.image.load("robot.png")
monster_image = pygame.image.load('monster.png')
coin_image = pygame.image.load('coin.png')

#Gives variable to the images widths, heights and determines their center for some images
robot_width_center = robot.get_width()/2
robot_height_center = robot.get_height() /2
x = 320 - robot_width_center 
y = 240 - robot_height_center 
coin_x = randint(0, window_width - coin_image.get_width()-70)
coin_y = randint(0, window_height - coin_image.get_height()-70)
caught_coins = 0 #Counter for the total of coins
coin_width_center = coin_x + coin_image.get_width()/2
coin_height_center = coin_y + coin_image.get_height()/2

monster_width = monster_image.get_width()
monster_height = monster_image.get_height()
monsters = [] #List in which the monster object are saved

#Robot movement
to_right = False
to_left = False
to_up = False
to_down = False

clock = pygame.time.Clock()
#Counter is a counter for each time the main loop is called, every 60 iterations the variable seconds increases 1
seconds = 0
counter = 0
#Variable to track a game over
over = False

#Font for the timer and coin scores
game_font = pygame.font.SysFont("Arial", 24)




while True:
    #Checks for a game over
    if over:
        game_over_font = pygame.font.SysFont("Arial", 60)
        game_over = game_over_font.render(f"GAME OVER", True, (255, 0, 0))
        text_rect = game_over.get_rect()
        game_over_x = window_width / 2 - text_rect.width / 2
        game_over_y = window_height/ 2 - text_rect.height / 2
        window.blit(game_over, [game_over_x, game_over_y])
    #Makes the game run
    else:
        if counter % 60 == 0:
            seconds += 1

        #If the robot grabs a coin the function is calles
        if get_coin(x, y, robot_width_center, robot_height_center, coin_width_center, coin_height_center):
            coin_x = randint(0, window_width - coin_image.get_width()-70) #Gives new coordinates to coin
            coin_y = randint(0, window_height - coin_image.get_height()-70) #Gives new coordinates to coin
            caught_coins += 1 #Increases caught coins
            coin_width_center = coin_x + coin_image.get_width()/2 #Recalculates the coin center
            coin_height_center = coin_y + coin_image.get_height()/2 #Recalculates the coin center

        #Robot movement
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    to_left = True
                if event.key == pygame.K_RIGHT:
                    to_right = True
                if event.key == pygame.K_UP:
                    to_up = True
                if event.key == pygame.K_DOWN:
                    to_down = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    to_left = False
                if event.key == pygame.K_RIGHT:
                    to_right = False
                if event.key == pygame.K_UP:
                    to_up = False
                if event.key == pygame.K_DOWN:
                    to_down = False


        #Makes the robot stay inside the screen
        if to_right and x <= window_width - robot.get_width():
            x += 2
        if to_left and x >= 0:
            x -= 2
        if to_up and y >= 0:
            y -= 2
        if to_down and y <= window_height - robot.get_height():
            y += 2

        ##Monster 
        #Monster appears every 3 seconds and at the beginning of the game
        if (seconds % 3 == 0 or seconds == 0) and counter % 60 == 0:
            new_monster = Monster(monster_width, monster_height)
            new_monster.appear(window_width, window_height)
            monsters.append(new_monster)
        if counter == 5:
            new_monster = Monster(monster_width, monster_height)
            new_monster.appear(window_width, window_height)
            monsters.append(new_monster)
        for monster in monsters:
            monster.pursue(x, y)
            if monster.catch(x,y):
                over = True

        #Generates the robot, coins, monsters, coin counter and timer
        window.fill((255, 255, 255))
        window.blit(robot, (x, y))
        window.blit(coin_image, (coin_x, coin_y))
        coins_text = game_font.render(f"Coins: {caught_coins}", True, (0, 0, 0))
        timer = game_font.render(f"Time: {seconds}", True, (0, 0, 0))
        window.blit(coins_text, (window_width-120, 10))
        window.blit(timer, (30, 15))
        for monster in monsters:
            window.blit(monster_image, (monster.x, monster.y))

    clock.tick(60)
    pygame.display.flip()
    counter += 1
    if event.type == pygame.QUIT:
        exit()  