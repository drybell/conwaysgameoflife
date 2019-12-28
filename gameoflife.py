# Daniel Ryaboshapka 
# December 26 2019
# gameoflife.py

# Running first version of conways game of life. 

############################################################# 
#                										    #
#						  RULES							    #
#														    #
#	 1. Live cells with 2-3 live neighbors stay alive       #
#	 2. >3 <2 live neighbors kill the cell 				    #
#	 3. Dead cells with exactly 3 live neighbors is live    #
#														    #
#############################################################

# width = number of columns
# height = number of rows

import numpy as np
from time import sleep
from copy import deepcopy

np.set_printoptions(threshold=np.inf)

class Board:

	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.board = np.zeros((width, height))

def setInitialBoard(x, initial_conditions):
	for pair in initial_conditions:
		x.board[pair[0],pair[1]] = 1

def gather_neighbors(row, column, x):
	max_width = x.width
	max_height = x.height
	live_counter = 0

	# all 8 navigable positions
	north = (row - 1 , column)
	north_east = (row - 1, column + 1)
	east = (row, column + 1)
	south_east = (row + 1, column + 1)
	south = (row + 1, column)
	south_west = (row + 1, column - 1)
	west = (row, column - 1)
	north_west = (row - 1, column - 1)

	navigation = [north, north_east, east, south_east, south, south_west, west, north_west]

	ctr = 0
	for position in navigation:
		# check if we're out of bounds (below 0 or above max - 1)
		if position[0] < 0 or position[1] < 0 or position[0] == max_height or position[1] == max_width:
			navigation[ctr] = (-1, -1)
		
		ctr += 1

	return navigation

# make a temp board that is a copy of the current board,
# with the location of the new cells calculated in simultime 
# to adhere to Conway's rules
def transition(x):
	y = deepcopy(x)
	for row in range(0, x.height):
		for column in range(0, x.width): 
			curr = x.board[row, column]
			nav = gather_neighbors(row, column, x)
			# if dead 
			live_counter = 0
			if curr == 0: 
				#check for 3 live neighbors 
				for live_cell in nav: 
					if live_cell == [-1, -1]:
						pass
					if x.board[live_cell[0], live_cell[1]] == 1:
						live_counter += 1
				if live_counter == 3: 
					y.board[row, column] = 1 
			elif curr == 1: 
				live_counter = 0
				#check for 2-3 live neighbors 
				for live_cell in nav:
					if live_cell == [-1, -1]:
						pass
					if x.board[live_cell[0], live_cell[1]] == 1:
						live_counter += 1
				if live_counter < 2 or live_counter > 3: 
					y.board[row, column] = 0
				else:
					y.board[row, column] = 1
			else:
				y.board[row, column] = 0
	return y 

def main():

	# use this to modify initial height and width of board
	width = 17
	height = 17

	x = Board(width, height)

	#list of coordinates that will be flipped to 1 

	#simple glider -- uncomment line below 
	# initial_conditions = ((5,5) , (6,6) , (6,7) , (5, 7) , (4 , 7))

	#simple toad -- uncomment line below 
	# initial_conditions = ((3,3) , (3,4) , (3,5), (2, 4) , (2, 5) , (2, 6))

	#penta-decathlon -- uncomment line below 
	initial_conditions = ((3,3),(3,4),(3,5),(4,4),(5,4),(6,3),(6,4),(6,5),(8,3),(8,4),(8,5),(9,3),(9,4),(9,5),(11,3),(11,4),(11,5),(12,4),(13,4),(14,3),(14,4),(14,5))

	#pulsar oscillator


	setInitialBoard(x, initial_conditions)
	print(x.board)

	# set the number of ticks and refresh rate
	max_ticks = 1000
	sleep_time = .1

	for i in range(0, max_ticks):
		y = transition(x)
		print(y.board)
		x = y

		sleep(sleep_time)

if __name__ == '__main__':
	main()