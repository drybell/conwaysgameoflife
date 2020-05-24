import pygame
from pygame.locals import *
from gameoflife import * 

pygame.init()

# use this to modify initial height and width of board
width = 100
height = 100

x = Board(width, height)

#list of coordinates that will be flipped to 1 

#simple glider -- uncomment line below 
# initial_conditions = ((5,5) , (6,6) , (6,7) , (5, 7) , (4 , 7))

#simple toad -- uncomment line below 
# initial_conditions = ((3,3) , (3,4) , (3,5), (2, 4) , (2, 5) , (2, 6))

#penta-decathlon -- uncomment line below 
# initial_conditions = ((3,3),(3,4),(3,5),(4,4),(5,4),(6,3),(6,4),(6,5),(8,3),(8,4),(8,5),(9,3),(9,4),(9,5),(11,3),(11,4),(11,5),(12,4),(13,4),(14,3),(14,4),(14,5))

#pulsar oscillator

#R-pentomino
# initial_conditions = ((3,3),(3,4),(2,4),(2,5),(4,4))

#R-pentomino centered 
# initial_conditions = ((50,50),(50,51),(49,51),(49,52),(51,51))

#Gosper Glider Gun
initial_conditions = ((80,2),(80,3),(81,2),(81,3),(80,12),(81,12),(82,12),(83,13),(84,14),(84,15),(79,13),(78,14),(78,15),(81,16),(81,18),(81,19),(82,18),(80,18),(79,17),(83,17),(80,22),(79,22),(78,22),(80,23),(79,23),(78,23),(77,24),(77,26),(76,26),(81,24),(81,26),(82,26),(79,36),(78,36),(79,37),(78,37))

#Gosper Gun starting higher up
initial_conditions2 = ((position[0] - 70, position[1]) for position in initial_conditions)

#block-laying switch engine
# initial_conditions = ((4,4),(5,4),(4,5),(4,6),(4,8),(6,8),(6,7),(7,5),(7,8),(8,4),(7,6),(8,6),(8,8))

# initial_conditions2 = ((position[0] + 30, position[1] + 30) for position in initial_conditions)




setInitialBoard(x, initial_conditions2)

# set the number of ticks and refresh rate
max_ticks = 1000
sleep_time = .1


# #pygame messing
# pygame.init()
# screen_width = 500
# screen_height = 500
# screen=pygame.display.set_mode([screen_width,screen_height])
# screen.fill((1,1,1))
# pygame.draw.rect(screen, (230, 40, 50), Rect((10,10),(20,20)))
# pygame.display.update()



window = pygame.display.set_mode([width,height], flags=pygame.RESIZABLE)

red = (230,50,50)
white = (255,255,255)
black = (0,0,0)

while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()

	window.fill(black)
	for row in range(0, x.height):
		for column in range(0, x.width): 
			if x.board[row, column] == 1:
				pygame.draw.rect(window, white, Rect((column, row), (1,1)))
	y = transition(x)
	x = y

	pygame.display.update()