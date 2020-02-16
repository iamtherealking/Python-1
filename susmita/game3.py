import pygame
pygame.init()
x=0
y=0
screen=pygame.display.set_mode((900,600))
background_image=pygame.image.load('road.png').convert()
running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
             running=False
    screen.fill((0,0,0))
    pygame.display.update()