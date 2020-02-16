import pygame
rect_colors =[(255,0,0),(0,255,0),(0,0,255)]
gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('color changer')
start_color =0
running = True
while running:
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            X,Y = pygame.mouse.get_pos()
            if((X >=400 and X <= 500) and (Y >=300 and Y <= 500)):
                start_color =start_color  + 1 if start_color < 2 else 0
    gameDisplay.fill((255,255,255))
    gameDisplay.fill(rect_colors[start_color],rect=[400,300,100,200])
    pygame.display.update()