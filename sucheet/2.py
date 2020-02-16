import pygame
pygame.init()
x=0
y=0
screen=pygame.display.set_mode((900,600))
background_img= pygame.image.load('road.png').convert()
running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running =False
    screen.blit(background_img,(x,y))
    pygame.display.update( )        