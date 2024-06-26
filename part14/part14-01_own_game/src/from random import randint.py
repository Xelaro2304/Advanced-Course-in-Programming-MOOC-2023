import pygame
import random
pygame.init()
window = pygame.display.set_mode((840, 680))
    
robot = pygame.image.load("robot.png")
monster_image = pygame.image.load("monster.png")
coin_image =pygame.image.load("coin.png")
    
    
x = 0
y = 480-robot.get_height()
    
    
robot_rect = robot.get_rect() 
    
to_right = False
to_left = False
    
    
robot_width, robot_height = robot.get_size()
    
robot_rect.y = y
    
points=0
points_rank = [10]
    
coins_collected = 0
    
game_font = pygame.font.SysFont("arial", 18)
    
    
    
    
class Coin:
    def __init__(self):
        self.rect = coin_image.get_rect()
        self.rect.x = random.randint(0, 840 -self.rect.width)
        self.rect.y = 480 - self.rect.height        
        
class Bullet:
    def __init__(self, x, y):
        self.radius = 10
        self.rect = pygame.Rect(x - self.radius, y - self.radius, 2* self.radius, 2*self.radius)
        self.speed = 5
    
    def move(self):
        self.rect.y -= self.speed
    
    def draw(self):
        pygame.draw.circle(window, (255, 255, 255), self.rect.center, self.radius)
    
    
bullets = []
    
class Bullet_coin:
    def __init__(self, x, y, direction):
        self.radius = 10
        self.rect = pygame.Rect(x - self.radius, y - self.radius, 2 * self.radius, 2 * self.radius)
        self.speed = 5
        self.direction = direction 
    def move(self):
        if self.direction == "left":
            self.rect.x -=self.speed
        elif self.direction == "right":
            self.rect.x += self.speed
    
    def draw(self):
        pygame.draw.circle(window, (255, 255, 0), self.rect.center, self.radius)
    
bullet_coins =[]
    
class Monster:
    def __init__(self, x, y):
        self.rect = monster_image.get_rect()
        self.x = x
        self.y = y
        self.direction = "down"
    
    def move(self):
        if self.direction == "down":
            self.y += 1
            self.rect.y = self.y
            self.rect.x = self.x
monsters =[]
    
coins =[]
    
clock = pygame.time.Clock()
    
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_left = True
            if event.key == pygame.K_RIGHT:
                to_right = True
            if event.key == pygame.K_SPACE:
                new_bullet =Bullet(x + robot_width // 2, y)
                bullets.append(new_bullet)
            if event.key == pygame.K_c:
                if coins_collected > 0:   
                    new_bullet_coin =Bullet_coin(x + robot_width // 2, y, "right")
                    bullet_coins.append(new_bullet_coin)
                    coins_collected -=1
            if event.key == pygame.K_x:
                if coins_collected > 0:
                    new_bullet_coin =Bullet_coin(x + robot_width // 2, y, "left")
                    bullet_coins.append(new_bullet_coin)           
                    coins_collected -=1  
    
            #new game:
            if event.key == pygame.K_F1:
                if len(monsters) > 0:
                    monsters.remove(monster)
                points = 0
                monsters = []
                x = 0 
                y = 480-robot.get_height()
                coins = []
                coins_collected = 0
                points_rank = [10] 
    
            #exit game
            if event.key == pygame.K_F2:
                exit()                
    
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                to_left = False
            if event.key == pygame.K_RIGHT:
                to_right = False
            
    
        
    
        if event.type == pygame.QUIT:
            exit()
    
    
    
    
    #moving the robot
    if to_right and x + robot_width < window.get_width():
        x += 4
        
    elif to_left and x > 0:
        x -= 4
    robot_rect.x = x
    
    #creating monsters
    if random.randint(0, 250) < 2 + points // 10:
        new_rock = Monster(random.randint(0, 640 - 50), -50)
        monsters.append(new_rock)
    
    #drawing
    window.fill((0, 0, 255)) 
    pygame.draw.rect(window, (255, 255, 255), (0, 480, 880, 200))
    pygame.draw.polygon(window, (0, 153, 0), [(500, 480), (600, 480), (550, 300)])
    pygame.draw.polygon(window, (0, 153, 0), [(200, 480), (300, 480), (250, 300)])
    text_rectangle = pygame.draw.rect(window, (0, 255, 0), (740, 200, 100, 50))
    pygame.draw.circle(window, (226, 226, 226), (750, 460), 20)
    pygame.draw.circle(window, (240, 236, 236), (750, 430), 12)
    pygame.draw.circle(window, (0, 0, 0), (746, 427), 2)
    pygame.draw.circle(window, (0, 0, 0), (755, 427), 2)
    pygame.draw.circle(window, (255, 0, 0), (750, 433), 2)
    pygame.draw.polygon(window, (255, 51, 51), [(740, 419), (760, 419), (750, 398)])
    
    #monster collisions 
    for monster in monsters.copy():
        monster.move()
        window.blit(monster_image, (monster.rect.x, monster.rect.y))
        if monster.rect.colliderect(robot_rect):
            monsters.remove(monster)
            points = 0
            monsters = []
            x = 0 
            y = 480-robot.get_height()
            coins = []
            coins_collected = 0
            points_rank = [10] 
        if monster.rect.bottom > 480:
            monsters.remove(monster)
            points = 0
            monsters = []
            x = 0
            y = 480-robot.get_height()
            coins = []
            coins_collected = 0
            points_rank = [10] 
    
    #game texts 
    text = game_font.render(f"Points {points}", True, (255, 0, 0))
    text2 = game_font.render(f"Coins {coins_collected}", True, (255, 0, 0))
    text3 = game_font.render(f"{7 - coins_collected} coins to win!", True, (255, 0, 0))
    text_rect = text3.get_rect()
    text_rect.center =  text_rectangle.center
    text_controls1= game_font.render(f"-'Spacebar' to shoot snowballs vertically (infinite ammo)", True, (153, 0, 0))
    text_controls2= game_font.render(f"-'x' and 'c' to shoot your coins horizontally (you lose your coins with every shot)", True, (153, 0, 0))
    text_controls3= game_font.render(f"-left and right arrows to move the robot hero", True, (153, 0, 0))
    text_controls4= game_font.render(f"-'f1' for new game", True, (153, 0, 0))
    text_controls5= game_font.render(f"-'f2' for exit game", True, (153, 0, 0))
    text_controls6= game_font.render(f"CONGRATULATIONS! YOU WIN!", True, (255, 0, 0))
    
    #bullet logics
    for bullet in bullets:
        bullet.move()
        bullet.draw()
        if bullet.rect.y < 0:
            bullets.remove(bullet)
    
    for bullet in bullets:
        for monster in monsters:
            if bullet.rect.colliderect(monster.rect):
                bullets.remove(bullet)
                monsters.remove(monster)
    
                points += 1  
    for bullet_coin in bullet_coins:
        bullet_coin.move()
        bullet_coin.draw()
        if bullet_coin.rect.x < 0 or bullet_coin.rect.x > window.get_width():
            bullet_coins.remove(bullet_coin)
    
    for bullet_coin in bullet_coins:
        for monster in monsters:
            if bullet_coin.rect.colliderect(monster.rect):
                monsters.remove(monster)
    
    #adding coins
    if points in points_rank:
        new_coin = Coin()
        coins.append(new_coin)
        points_rank[0] = points_rank[0] + 10 
    
    
    for coin in coins:
        window.blit(coin_image, (coin.rect.x, coin.rect.y))
        if coin.rect.colliderect(robot_rect):
            coins.remove(coin)
            coins_collected +=1
    
    
    
    window.blit(robot, (x, y))
    window.blit(text, (740, 100))
    window.blit(text2, (740, 150))
    if coins_collected < 7:
        window.blit(text3, text_rect.topleft)
    window.blit(text_controls1, (240, 560))
    window.blit(text_controls2, (240, 600))
    window.blit(text_controls3, (240, 640))
    window.blit(text_controls4, (60, 560))
    window.blit(text_controls5, (60, 600))
    if coins_collected > 6:
        monsters =[]
        window.blit(text_controls6, (300, 260))
        coins_collected = 100
        
                
    
    pygame.display.flip()
    
    clock.tick(60)
    
    
#The code runs well in this version. However when I tried to create a class with the name of the game ("SnowRobotHero"),
#it gave me a weird problem: the screen was getting dark every time I shot. For that reason, I don't
#include the main class in this code. Another problem that I have is that I can't load the images
#just using "image_name_example.png" (I don't know why) but it works when I put the relative
#path 'r"src\image_name_example.png"'. I suppose that if you have any problem with the loading of the images
#you can just change the r"src\image_name_example.png" to the simple "image_name_example.png"
#  I hope you enjoy it!! 