##
#
# Traveling Salesman brute-force solution

G = {'A':[('B', 1), ('C', 5), ('D', 4)], 'B':[('A', 1), ('C', 2), ('D', 3)],
	 'C':[('A', 5), ('B', 2), ('D', 3)], 'D':[('A', 4), ('B', 6), ('C', 3)]}

'''

Picture of G

	    1
  A-----------B
  |			  |
4 |			  | 2
  |			  | 
  |			  |
  D-----------C
	    3
diagonals (not drawn) are

		AC = 5
		BD = 6
 
tsp(G) = 1+2+3+4 = 10
'''


from itertools import permutations

def d(G, v1, v2):
	# returns the distance between v1 and v2 in a graph
	# G is adjacency list = {v:[(v1, d1)]}
	for i in range(len(G[v1])):
		if G[v1][i][0] == v2:
			return G[v1][i][1]

def tsp(G):
	# G is adjacency list
	size = len(G)
	min_w = 100000 # this will store the current minimum weighted path
	best_path = () # this will store the best path
	for path in permutations(G):
		# iterate through all possible orders in which vertices can be visited
		w = 0 # weight of the path
		for i in range(size):
			if i == size-1:
				# the last one
				# complete the cycle by connecting the first and last vertices visited
				w += d(G, path[0], path[-1])
			else:
				w += d(G, path[i], path[i+1])
		if w < min_w:
			# if this new path is better than the previous, replace
			min_w = w
			best_path = path

	return best_path, min_w

# print(tsp(G))



