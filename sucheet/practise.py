import time
import pygame
import random
pygame.init()
#############
crash_sound = pygame.mixer.Sound("crash.wav")
#############
display_width = 800
display_height = 600
black = (0,0,0)
white = (255,255,255)
red = (200,0,0)
green = (0,200,0)
bright_red = (255,0,0)
bright_green = (0,255,0)
block_color = (53,115,255)
car_width = 73
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('A bit Racey')
clock = pygame.time.Clock()
carImg = pygame.image.load('racecar.png')
gameIcon = pygame.image.load('carIcon.png')
pygame.display.set_icon(gameIcon)
pause = False
#crash = True
def things_dodged(count):
font = pygame.font.SysFont("comicsansms", 25)
text = font.render("Dodged: "+str(count), True, black)
gameDisplay.blit(text,(0,0))
def things(thingx, thingy, thingw, thingh, color):
pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])
def car(x,y):
gameDisplay.blit(carImg,(x,y))
def text_objects(text, font):
textSurface = font.render(text, True, black)
return textSurface, textSurface.get_rect()
def crash():
####################################
pygame.mixer.Sound.play(crash_sound)
pygame.mixer.music.stop()
####################################
largeText = pygame.font.SysFont("comicsansms",115)
TextSurf, TextRect = text_objects("You Crashed", largeText)
TextRect.center = ((display_width/2),(display_height/2))
gameDisplay.blit(TextSurf, TextRect)
while True:
for event in pygame.event.get():
if event.type == pygame.QUIT:
pygame.quit()
quit()
button("Play Again",150,450,100,50,green,bright_green,game_loop)
button("Quit",550,450,100,50,red,bright_red,quitgame)
pygame.display.update()
clock.tick(15) 
def button(msg,x,y,w,h,ic,ac,action=None):
mouse = pygame.mouse.get_pos()
click = pygame.mouse.get_pressed()
if x+w > mouse[0] > x and y+h > mouse[1] > y:
pygame.draw.rect(gameDisplay, ac,(x,y,w,h))
if click[0] == 1 and action != None:
action()         
else:
pygame.draw.rect(gameDisplay, ic,(x,y,w,h))
smallText = pygame.font.SysFont("comicsansms",20)
textSurf, textRect = text_objects(msg, smallText)
textRect.center = ( (x+(w/2)), (y+(h/2)) )
gameDisplay.blit(textSurf, textRect)
def quitgame():
pygame.quit()
quit()
def unpause():
global pause
pygame.mixer.music.unpause()
pause = False
def paused():
############
pygame.mixer.music.pause()
#############
largeText = pygame.font.SysFont("comicsansms",115)
TextSurf, TextRect = text_objects("Paused", largeText)
TextRect.center = ((display_width/2),(display_height/2))
gameDisplay.blit(TextSurf, TextRect)
while pause:
for event in pygame.event.get():
if event.type == pygame.QUIT:
pygame.quit()
quit()
button("Continue",150,450,100,50,green,bright_green,unpause)
button("Quit",550,450,100,50,red,bright_red,quitgame)
pygame.display.update()
clock.tick(15)   
def game_intro():
intro = True
while intro:
for event in pygame.event.get():
#print(event)
if event.type == pygame.QUIT:
pygame.quit()
quit()
gameDisplay.fill(white)
largeText = pygame.font.SysFont("comicsansms",115)
TextSurf, TextRect = text_objects("A bit Racey", largeText)
TextRect.center = ((display_width/2),(display_height/2))
gameDisplay.blit(TextSurf, TextRect)
button("GO!",150,450,100,50,green,bright_green,game_loop)
button("Quit",550,450,100,50,red,bright_red,quitgame)
pygame.display.update()
clock.tick(15)
def game_loop():
global pause
############
pygame.mixer.music.load('jazz.wav')
pygame.mixer.music.play(-1)
############
x = (display_width * 0.45)
y = (display_height * 0.8)
x_change = 0
thing_startx = random.randrange(0, display_width)
thing_starty = -600
thing_speed = 4
thing_width = 100
thing_height = 100
thingCount = 1
dodged = 0
gameExit = False
while not gameExit:
for event in pygame.event.get():
if event.type == pygame.QUIT:
pygame.quit()
quit()
if event.type == pygame.KEYDOWN:
if event.key == pygame.K_LEFT:
x_change = -5
if event.key == pygame.K_RIGHT:
x_change = 5
if event.key == pygame.K_p:
pause = True
paused()
if event.type == pygame.KEYUP:
if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
x_change = 0
x += x_change
gameDisplay.fill(white)
things(thing_startx, thing_starty, thing_width, thing_height, block_color)
thing_starty += thing_speed
car(x,y)
things_dodged(dodged)
if x > display_width - car_width or x < 0:
crash()
if thing_starty > display_height:
thing_starty = 0 - thing_height
thing_startx = random.randrange(0,display_width)
dodged += 1
thing_speed += 1
thing_width += (dodged * 1.2)
if y < thing_starty+thing_height:
print('y crossover')
if x > thing_startx and x < thing_startx + thing_width or x+car_width > thing_startx and x + car_width < thing_startx+thing_width:
print('x crossover')
crash()
pygame.display.update()
clock.tick(60)
game_intro()
game_loop()
pygame.quit()
quit()

 Helicopter Game :
import time
import pygame
from random import randint,randrange
black = (0,0,0)
white = (255,255,255)
sunset = (253,72,47)
greenyellow = (184,255,0)
brightblue = (47,228,253)
orange = (255,113,0)
yellow = (255,236,0)
purple = (252,67,255)
colorChoices = [greenyellow,brightblue,orange,yellow,purple]
pygame.init()
surfaceWidth = 800
surfaceHeight = 500
imageHeight = 43
imageWidth = 100
surface = pygame.display.set_mode((surfaceWidth,surfaceHeight))
pygame.display.set_caption('Helicopter')
clock = pygame.time.Clock()
img = pygame.image.load('Helicopter.png')
def score(count):
font = pygame.font.Font('freesansbold.ttf', 20)
text = font.render("Score: "+str(count), True, white)
surface.blit(text, [0,0])
def blocks(x_block, y_block, block_width, block_height, gap, colorChoice):
pygame.draw.rect(surface, colorChoice, [x_block,y_block,block_width,block_height])
pygame.draw.rect(surface, colorChoice, [x_block,y_block+block_height+gap,block_width, surfaceHeight])
def replay_or_quit():
for event in pygame.event.get([pygame.KEYDOWN, pygame.KEYUP, pygame.QUIT]):
if event.type == pygame.QUIT:
pygame.quit()
quit()
elif event.type == pygame.KEYDOWN:
continue
return event.key
return None
def makeTextObjs(text, font):
textSurface = font.render(text, True, sunset)
return textSurface, textSurface.get_rect()
def msgSurface(text):
smallText = pygame.font.Font('freesansbold.ttf', 20)
largeText = pygame.font.Font('freesansbold.ttf', 150)
titleTextSurf, titleTextRect = makeTextObjs(text, largeText)
titleTextRect.center = surfaceWidth / 2, surfaceHeight / 2
surface.blit(titleTextSurf, titleTextRect)
typTextSurf, typTextRect = makeTextObjs('Press any key to continue', smallText)
typTextRect.center =  surfaceWidth / 2, ((surfaceHeight / 2) + 100)
surface.blit(typTextSurf, typTextRect)
pygame.display.update()
time.sleep(1)
while replay_or_quit() == None:
clock.tick()
main()
def gameOver():
msgSurface('crashed!')
def helicopter(x, y, image):
surface.blit(img, (x,y))
def main():
x = 150
y = 200
y_move = 0
x_block = surfaceWidth
y_block = 0
block_width = 75
block_height = randint(0,(surfaceHeight/2))
gap = imageHeight * 3
block_move = 4
current_score = 0
blockColor = colorChoices[randrange(0,len(colorChoices))]
game_over = False
while not game_over:
for event in pygame.event.get():
if event.type == pygame.QUIT:
game_over = True
if event.type == pygame.KEYDOWN:
if event.key == pygame.K_UP:
y_move = -5
if event.type == pygame.KEYUP:
if event.key == pygame.K_UP:
y_move = 5
y += y_move
surface.fill(black)
helicopter(x ,y, img)
blocks(x_block, y_block, block_width, block_height, gap, blockColor)
score(current_score)
x_block -= block_move
if y > surfaceHeight-40 or y < 0:
gameOver()
if x_block < (-1*block_width):
x_block = surfaceWidth
block_height = randint(0, (surfaceHeight / 2))
blockColor = colorChoices[randrange(0,len(colorChoices))]
current_score+=1
if x + imageWidth > x_block:
if x < x_block + block_width:
if y < block_height:
if x - imageWidth < block_width + x_block:
gameOver()
if x + imageWidth > x_block:
if y + imageHeight > block_height+gap:
if x < block_width + x_block:
gameOver()
#if x_block < (x - block_width) < x_block + block_move:
#    current_score += 1
if 3 <= current_score < 5:
block_move = 5
gap = imageHeight * 2.9
if 5 <= current_score < 8:
block_move = 6
gap = imageHeight *2.8
if 8 <= current_score < 14:
block_move = 7
gap = imageHeight *2.7
pygame.display.update()
clock.tick(60)
main()
pygame.quit()
quit()