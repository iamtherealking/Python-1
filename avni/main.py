import pygame
#initializes pygame
pygame.init()

player_img= pygame.image.load('C:/Users/User/Desktop/game-sprite.png')
playerX = 370
playerY = 480

game_screen = pygame.display.set_mode((800,600))
def player(x,y) :
	game_screen.blit(player_img, (x,y))
running = True

while running:
	game_screen.fill((255,165,0))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
			
	player(playerX, playerY)
	playerX = playerX + 0.1
	pygame.display.update();