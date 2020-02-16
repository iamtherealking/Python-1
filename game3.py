import pygame
pygame.init()
x=0
y=0
#background_img = pygame.image.load('road.png')
screen = pygame.display.set_mode((900,600))
background_img = pygame.image.load('/Users/suman/Desktop/road.png')
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(background_img,(x,y))    
    pygame.display.update()      