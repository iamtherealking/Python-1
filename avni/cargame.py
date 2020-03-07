import pygame
import time
import random
pygame.init()
x=0
start_time=time.time()
y=0
screen_width = 900
screen_height = 600
flag=2
car_width=94
lane_width=900/3
enemies = []
enemy_y=-200
player_y=400
player_height=200
#player_x=flag*lane_width-(lane_width+player_width)/2
screen = pygame.display.set_mode((screen_width,screen_height))
background_image=pygame.image.load('road.png').convert()
front_image= pygame.image.load('game_sprite.png').convert_alpha()#car ko shadow hatauna alpha use gareko
enemy_image=pygame.image.load('enemy.png').convert_alpha()
def bkmovement(road_x,road_y,screen,road_image,screen_height):# to change background we can pass argument

    rel_y=road_y % screen_height# argument ko j sukai name rakhe pani tala real name bhayepaxi farak pardaina
    screen.blit(background_image,(road_x,rel_y-screen_height))
    if rel_y<screen_height:
        screen.blit(background_image,(road_x,rel_y))
    road_y=road_y+10
    return road_y
def car_collision(enemies,player_height,player_y,flag):
    for enemy in enemies:
        if enemy[2]==flag and enemy[1]+player_height>=player_y:
            print('collision')
def generate_enemies(enemy_y,lane_width,enemies,car_width):
    flag = random.randrange(1,4,1)
    enemies.append([int(flag * lane_width - (lane_width + car_width)/2),enemy_y,flag])

def enemy_movement(enemies,game_screen,enemy_img):
    if len(enemies)<=0: return
    for enemy in enemies:
        game_screen.blit(enemy_img,(enemy[0],enemy[1]))
        enemy[1]+=10

def splice_enemies(enemies):
    for enemy in enemies:
        if enemy[1]>=600:
            index_enemy=enemies.index(enemy)
            enemies.pop(index_enemy)
    return enemies

running=True

while running:
    car_collision(enemies,player_height,player_y,flag)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            if event.key == pygame.K_LEFT  or event.key == ord('a'):

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
        start_time=time.time()
        generate_enemies(enemy_y,lane_width,enemies,car_width)
    y=bkmovement(x,y,screen,background_image,screen_height)
    screen.blit(front_image,(player_x,player_y))
    enemy_movement(enemies,screen,enemy_image)
    pygame.display.update()
    enemies=splice_enemies(enemies)
