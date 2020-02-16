import pygame
game_screen = pygame.display.set_mode((1000 , 600))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
			pass
    game_screen.fill((255,255,255))
    pygame.display.update()
