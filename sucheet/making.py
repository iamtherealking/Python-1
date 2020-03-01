import pygame
pygame.init()
x=0
y=0
flag=2
car_width=94
car_length=200
lane_width=300
playery=400
#player_X=flag*lane_width-(lane_width+car_width)/2

screen_height=600
screen_width=900
screen=pygame.display.set_mode((screen_width,screen_height))
background_img= pygame.image.load('road.png').convert()
player_img=pygame.image.load("game_sprite.png").convert_alpha()
running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running =False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT or event.key==pygame.K_a:
                if flag<=1:
                    continue
                flag-=1
            if event.key==pygame.K_RIGHT or event.key==pygame.K_d: 
                if flag>=3:
                    continue
                flag+=1
        if event.type==pygame.KEYUP:
            pass          
    rel_y=y%screen_height
    #print(rel_y)        
    screen.blit(background_img,(x,rel_y-screen_height))
    #print("rel_y-height{}".format(rel_y-screen_height))
    if rel_y<screen_height:
        screen.blit(background_img,(x,rel_y))
    y=y+0.5
    player_X=flag*lane_width-(lane_width+car_width)/2
    screen.blit(player_img,(player_X,playery))
    #print(y)
    pygame.display.update( ) 