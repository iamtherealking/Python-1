import pygame
screen = pygame.display.set_mode((1000,800))
running = True
while running:
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            running = False
    screen.fill((255,0,0))
    pygame.display.update()
