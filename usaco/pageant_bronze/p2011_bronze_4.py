#
#
#
#

import sys

sys.setrecursionlimit(1000000)


def flood_fill(matrix, start, label):
	dimensions = (len(matrix)-1, len(matrix[0])-1)
	if not 0 <= start[0] <= dimensions[0] or not 0 <= start[1] <= dimensions[1]:
		return
	elif matrix[start[0]][start[1]] != 'X':
		return
	matrix[start[0]][start[1]] = label

	flood_fill(matrix, (start[0]+1, start[1]), label)
	flood_fill(matrix, (start[0]-1, start[1]), label)
	flood_fill(matrix, (start[0], start[1]+1), label)
	flood_fill(matrix, (start[0], start[1]-1), label)

def determine_regions(matrix):
	r1_start = ()

	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			if matrix[i][j] == 'X':
				r1_start = (i, j)
	flood_fill(matrix, r1_start, 'Y')

def min_dist(matrix):
	r1 = []
	r2 = []
	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			if matrix[i][j] == 'X':
				r1.append((i, j))
			elif matrix[i][j] == 'Y':
				r2.append((i, j))
	minimum = 1000
	for x in r1:
		for y in r2:
			distance = abs(x[0]-y[0]) + abs(x[1]-y[1])
			if distance < minimum:
				minimum = distance
	return minimum-1

def create_matrix(lines):
	# the first lines specify len(matrix) and len(matrix[0]) respectively
	matrix = []
	for i in lines[1:]:
		matrix.append(list(i[:-1]))
	return matrix

f = open('I.6', 'r')
lines = f.readlines()
f.close()

m = create_matrix(lines)
determine_regions(m)
result = min_dist(m)

out = open('pageant.out', 'w')
out.write(str(result))
out.close()
	
		

