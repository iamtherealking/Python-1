import pygame
pygame.init()
screen=pygame.display.set_mode((1000,800))
running = True
while running:
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            running = False 
        if event.type == pygame.MOUSEBUTTONDOWN:
            screen.fill((240,248,255))  
    pygame.display.update()      