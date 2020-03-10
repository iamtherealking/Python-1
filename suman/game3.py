import pygame
import time
import random
pygame.init()
start_time = time.time()
font_1 = pygame.font.SysFont('comic sans MS',50)
font_2 = pygame.font.SysFont('comic sans MS',30)
font_3 = pygame.font.SysFont('comic sans MS',30)
x=0
y=0
flag = 2
car_width = 94
lane_width = 900/3
enemy_y = -100
player_y = 400
screen_width=900
screen_height=600
enemies = [ ]
player_height = 200
gameover = False
score = 0
#background_img = pygame.image.load('road.png')
screen = pygame.display.set_mode((screen_width,screen_height))
background_img = pygame.image.load('/Users/suman/Desktop/road.png')
player_img = pygame.image.load('/Users/suman/Desktop/game_sprite.png')
enemy_img = pygame.image.load('/Users/suman/Desktop/enemy.png')
def move_background(road_x,road_y,screen_height,screen,road_img):
    rel_y=road_y%screen_height
    #print("rel_y {}".format(rel_y))
    screen.blit(road_img,(road_x,rel_y-screen_height))  
    #print("rel_y-height {}".format(rel_y-screen_height))
    if rel_y<screen_height:
        screen.blit(road_img,(x,rel_y))
    road_y+=10
    return road_y

def game_over_screen(screen,font1,font2):
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    waiting = False
        screen.fill((0,0,0))
        game_over_message = font1.render('GAMEOVER',False,(100,0,34))
        click_to_try_again = font2.render('Press spacebar to try again',False,(100,0,34))
        screen.blit(game_over_message,(300,100))
        screen.blit(click_to_try_again,(200,300))
        pygame.display.update()

def generate_enemies(enemy_y,lane_width,enemies,car_width):
    flag = random.randrange(1,4,1)
    enemies.append([int(flag * lane_width - (lane_width + car_width)/2),enemy_y,flag])

def enemy_moment(enemies,game_screen,sprite_img):
    if len(enemies)<=0 : return
    for enemy in enemies:
        game_screen.blit(sprite_img,(enemy[0],enemy[1]))
        enemy[1]+=10
def splice_enemies(enemies,score):
    for enemy in enemies:
        if enemy[1]>=600:
            index_enemy = enemies.index(enemy)
            enemies.pop(index_enemy)
            score+=1
    return enemies,score
def car_collision(enemies,player_y,car_height,flag,gameover):
    for enemy in enemies:
        if enemy[2]==flag and enemy[1]+player_height>=player_y:
            gameover = True
            return gameover
            

running = True
while running: 
    gameover = True if car_collision(enemies,player_y,player_height,flag,gameover) else False
    if gameover:
        time.sleep(0.5)
        game_over_screen(screen,font_1,font_2)
        start_time = time.time()
        enemies = [ ]
        x=0
        y=0
        flag = 2
        gameover = False
        player_x =403
        enemy_y =-200
        score = 0

        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                if flag <= 1:
                    continue
                flag-=1
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                if flag >= 3:
                    continue
                flag+=1 
        if event.type == pygame.KEYUP:
            pass
        player_x =int( flag * lane_width - (lane_width + car_width)/2)
    if time.time()-start_time>3:
        start_time = time.time()
        generate_enemies(enemy_y,lane_width,enemies,car_width)
    y=move_background(x,y,screen_height,screen,background_img)
    score_display = font_3.render('score {}'.format(score),False,(255,255,255))
    screen.blit(score_display,(700,50))
    enemy_moment(enemies,screen,enemy_img)
    screen.blit(player_img,(player_x,player_y)) 
   # gameover = True if car_collision(enemies,player_y,player_height,flag,gameover) else False
    
    pygame.display.update()
    enemies,score=splice_enemies(enemies,score)
    
    