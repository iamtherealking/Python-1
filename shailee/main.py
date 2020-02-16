import pygame
#initialzies pygame
pygame.init()

player_img= pygame.image.load('/Users/shail/OneDrive/Desktop/game-sprite.png')
playerX = 370
playerY = 480

game_screen = pygame.display.set_mode((800,600))
def player(x,y) :
	game_screen.blit(player_img, (x,y))
running = True

while running:
	game_screen.fill((255,165,0))
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key== pygame.k_ESC:
				running = False

	playerX=playerX+0.5
	#playerY=playerY-0.1
	if playerX>=736:
		playerX=playerX-736

#playerX=playerX+736
player(playerX,playerY)
pygame.diaplay.update();