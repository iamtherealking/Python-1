import pygame
#Initializes pygame
pygame.init()																			
player_img = pygame.image.load('C:/Users/Dell/Desktop/game-sprite.png')
playerX	= 370
playerY	= 40
					
game_screen = pygame.display.set_mode((800,600))
def player(x,y) :
	game_screen.blit(player_img,(x,y))

running	= True

while running:
	for event in pygame.event.get():
	game_screen.fill((0,0,0))
	game_screen.blit(player_img,(playerX,playerY))
	player(playerX, playerY)
	playerX = playerX + 0.1
	pygame.display.update()
	if event.type == pygame.QUIT:
		running = False
		
		
		

