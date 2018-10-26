#
#
#
#

from collections import deque
import time

'''
nodes = possible configurations
edges = links two configurations that can be obtained through changing one character
'''

def display(string):
	# displays the string of length 81 representing the puzzle into the sudoku format
	for i in range(len(string)):
		if i % 9 == 8:
			# we print starting on a new line every 9 characters
			print(string[i])
		else:
			# we print characters in groups of 9 on the same line
			print(string[i], end='')

def related(pos1, pos2):
	# determines if the characters at indices pos1 and pos2 are related
	# related meaning they are in the same 3x3 subsquare, row, or column
	# indices start at 0
	coors1 = (pos1%9, pos1//9)
	coors2 = (pos2%9, pos2//9)
	if coors1[0] == coors2[0] or coors1[1] == coors2[1]:
		# same row or column
		return True
	elif pos1//27 == pos2//27 and (pos1%9)//3 == (pos2%9)//3:
		# same 3x3 subsquare
		return True
	return False

def get_adjacent(string):
	# this function returns all the adjacent sudoku configurations
	adj = []
	for i in range(len(string)): # 81
		if string[i] == '.': # consider it only if its blank
			r = [] # get all numbers in the positions related to the current one
			for j in range(len(string)):
				if related(i, j):
					r.append(string[j])
			for num in range(1, 10): # number that will be entered
				# only enter the number if all the related positions do not contain it
				if str(num) not in r:
					adj.append(string[:i] + str(num) + string[i+1:])
			break
	return adj

def DFS(string):
	# uses DFS to solve the given sudoku puzzle
	l = deque()
	l.append(string)
	
	while l:
		puzzle = l.pop()
		if '.' not in puzzle:
			# the puzzle is solved
			return puzzle
		for neighbor in get_adjacent(puzzle):
			l.append(neighbor)

	return -1

f = open('99.txt', 'r')
lines = [l.strip() for l in f.readlines()]

for l in lines:
	start = time.perf_counter()
	display(DFS(l))
	end = time.perf_counter()
	print('Time:', end-start)




