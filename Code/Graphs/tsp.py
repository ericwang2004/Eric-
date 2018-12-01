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
	# O(V), since len(G[v1]) <= V
	for vertex, distance in G[v1]:
		if vertex == v2:
			return distance

def tsp(G):
	# G is adjacency list
	size = len(G)
	L =  list(G.keys())
	start = L[0]
	del L[0]
	min_w = 100000 # this will store the current minimum weighted path
	best_path = () # this will store the best path
	for path in permutations(L):

		# iterate through all possible orders in which vertices can be visited
		w = d(G, start, path[0]) # weight of the path
		for i in range(size-2):
			w += d(G, path[i], path[i+1])
		w += d(G, path[-1], start)
		if w < min_w:
			# if this new path is better than the previous, replace
			min_w = w
			best_path = path
		
	best_path = (start,) + best_path
	return best_path, min_w

# print(tsp(G))



