import pygame
pygame.init()
x=0
y=0
flag = 2
car_width = 94
lane_width = 900/3
player_y = 400
screen_width=900
screen_height=600
#background_img = pygame.image.load('road.png')
screen = pygame.display.set_mode((screen_width,screen_height))
background_img = pygame.image.load('/Users/suman/Desktop/road.png')
player_img = pygame.image.load('/Users/suman/Desktop/game_sprite.png')
running = True
while running:
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
    rel_y=y%screen_height
    #print("rel_y {}".format(rel_y))
    screen.blit(background_img,(x,rel_y-screen_height))  
    #print("rel_y-height {}".format(rel_y-screen_height))
    if rel_y<screen_height:
        screen.blit(background_img,(x,rel_y))
    y+=7
    player_x = flag * lane_width - (lane_width + car_width)/2
    screen.blit(player_img,(player_x,player_y))    
    pygame.display.update()
    