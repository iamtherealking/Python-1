import pygame
#Initializes pygame
pygame.init()

player_img = pygame.image.load('C:/Users/Acerr/Desktop/game-sprite.png')
playerX = 370
playerY = 480

game_screen = pygame.display.set_mode((800,600))
def player(x,y) :
	game_screen.blit(player_img,(x,y))
	
running = True

while running:
		game_screen.fill((0,0,0))
		for event in pygame.event.get():
			 if event.type == pygame.QUIT:
				 running = False
				 
		player(playerX,playerY)
		playerX = playerX +0.1
		pygame.display.update();
		
		game_screen.blit(player_img,(playerX,playerY))
		pygame.display.update();
		        	

					
