#a=[20,40,55,90]
#def temp(f):
#    c=((f-32)*5)/9
#    return c
#for i in range(4):
#    print(temp(a[i]))
   
#a={'apple':23,'banana':30,'carrot':10,'pineapple':70,'coconut':90,'mango':20}
#for i in a: either this or below code
#for i in a.items():
#    print(i)

#def sq_root(n):
#    s=n**0.5
#    return s
#sq_root(4)

import pygame
import time
import random

pygame.init()
x=0
start_time=time.time()
y=0
font_1 = pygame.font.SysFont('comic sans MS',50)
font_2 = pygame.font.SysFont('comic sans MS',30)
font_3 = pygame.font.SysFont('comic sans MS',20)
flag=2
lane_width=900/3
player_y=400
screen_height=600
screen_width=900
car_width=94
car_height=200
enemies = []
enemy_y = -200
gameover = False
score = 0
screen=pygame.display.set_mode((screen_width,screen_height))
background_image=pygame.image.load('road.png').convert()

car_img=pygame.image.load('car.png').convert_alpha()
enemy_img=pygame.image.load("enemy.png").convert_alpha()


def move_background(road_x,road_y,screen,road_image,screen_height):
    rel_y=road_y%screen_height

   # print("rel_y-screen_height {}".format(rel_y-screen_height))
    screen.blit(background_image,(road_x,(rel_y-screen_height))) 
    if (rel_y<screen_height):

        screen.blit(road_image,(road_x,rel_y))
    road_y+=1
    return road_y

def generate_enemies(enemy_y,lane_width,enemies,car_width):
     flag = random.randrange(1,4,1)
     enemies.append([int(flag * lane_width - (lane_width + car_width)/2),enemy_y,flag])

def enemy_moment(enemies,game_screen,sprite_img):
    if len(enemies)<=0 : return
    for enemy in enemies:
        game_screen.blit(sprite_img,(enemy[0],enemy[1]))
        enemy[1]+=1
def splice_enemies(enemies,score):
    for enemy in enemies:
        if enemy[1]>=600:
            index_enemy = enemies.index(enemy)
            enemies.pop(index_enemy)
            score+=1
    return enemies,score
def car_collision(enemies,player_y,car_height,flag,gameover):
    for enemy in enemies:
        if enemy[2] == flag and enemy[1]+car_height>=player_y:
            gameover = True
            return gameover

def game_over_screen(screen,font_1,font_2):
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.KEYUP:
             if event.key == pygame.K_SPACE:
                waiting = False
        screen.fill((0,0,0))

        game_over_message = font_1.render('GameOver',False,(0,150,255))

        click_to_try_again = font_2.render('press spacebar to try again',False,(1,151,154))



        screen.blit(game_over_message,(300,100))
        screen.blit(click_to_try_again,(200,300))
        pygame.display.update( )           



running=True
while running:
    gameover = True if car_collision(enemies,player_y,car_height,flag,gameover) else False
    if gameover:

        time.sleep(0.5)
        game_over_screen(screen,font_1,font_2)
        start_time = time.time()
        enemies = []
        x = 0
        y = 0
        player_x = 403
        player_y = 400
        flag = 2
        enemy_y = -200
        game_over = False
        score = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                if flag<=1:
                    continue
                flag-=1
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                if flag>=3:
                    continue
                flag+=1
        if event.type == pygame.KEYUP:
            pass  
        player_x=flag*lane_width-(lane_width+car_width)/2 
    if time.time()-start_time>3:
        start_time = time.time()
        generate_enemies(enemy_y,lane_width,enemies,car_width)
    y=move_background(x,y,screen,background_image,screen_height)      

    score_display = font_3.render('score.{}'.format(score),False,(1,250,250))
    screen.blit(score_display,(700,100))
    
    
    enemy_moment(enemies,screen,enemy_img)
    


    screen.blit(car_img,(player_x,player_y))
   # second_depends = time.time()-start_time
    #if second_depends==3:
     #   start_time=time.time()

    #screen.fill((0,0,0))

    gameover = True if car_collision(enemies,player_y,car_height,flag,gameover) else False
    pygame.display.update() 
    enemies,score = splice_enemies(enemies,score)           