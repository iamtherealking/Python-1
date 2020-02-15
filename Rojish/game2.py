import pygame

# initializes pygame
pygame.init()

player_img = pygame.image.load('game-sprite.png')

playerX = 370
playerY = 480

player_img = pygame.image.load('ugoo.png')
playerX = 100
playerY = 100
game_screen = pygame.display.set_mode((1080, 720))


def player(x, y):
    game_screen.blit(player_img, (x, y))


running = True

while running:
    game_screen.fill((256, 256, 256))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    playerX = playerX + 0.1
    if playerX >= 736:
        playerX = 0
    player(playerX, playerY)
    pygame.display.update()


