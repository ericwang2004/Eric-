# explain A*
#
#
#
#
#
#


from collections import deque
import time
from heapq import heappush, heappop

def timing(graph, start, end):
	s = time.perf_counter()
	BFS(graph, start, end)
	e = time.perf_counter()
	bfs_time = e-s

	s = time.perf_counter()
	DFS(graph, start, end)
	e = time.perf_counter()
	dfs_time = e-s

	s = time.perf_counter()
	A_Star(graph, start, end)
	e = time.perf_counter()
	astar_time = e-s

	print('The BFS time was {}'.format(bfs_time))
	print('The DFS time was {}'.format(dfs_time)) 
	print('The A* time was {}'.format(astar_time))

def BFS(graph, start, end):

    # determines whether there exists a path from start to end
    # graph is an adjacency list
	l = deque()					# queue l contains the current path
	l.append([start])			
	visited = set([start])		# set visited contains the visited vertices
	while l: # > 0
		# while l has elements		
		path = l.popleft()
		# let path be the first path in l
		if path[-1] == end:
			# here, we have reached the end vertex, so return the path
			return path
		visited.add(path[-1])
		# if not, then add this particular path to visited
		
		# for each neighbor of the last vertex in the path,
		# add it to the path only if it has not been visited already
		for neighbor in graph[path[-1]]:
			if neighbor not in visited:
				l.append(path + [neighbor])
	return -1 # if no path from start to end exists

def DFS(graph, start, end):
	# depth first, so l is a stack
	l = deque()
	l.append([start])
	visited = set([start])
	while l:
		path = l.pop()
		if path[-1] == end:
			return path
		visited.add(path[-1])
		for neighbor in graph[path[-1]]:
			if neighbor not in visited:
				l.append(path + [neighbor])
	return -1

def create_adjacency_list(lines):
	'''
	Runtime of create_adjacency_list
	
	first for loop
	loop runs V times because there are exactly V lines
		loop on runs a constant len(word) times
		if statement: O(V)
		total O(V^2)
	second for loop
	loop runs len(word)*V times
	'''
	adj = {} # what will be returned
	d = {} # contains pairs of "abc?ef":["abcaef", "abcbef", ...]
	# i.e. words that could replace the "?"
	for word in lines:
		# create the keys of adj
		word = word.strip()
		adj[word] = []
		for i in range(len(word)):
			# populate d in these 5 lines
			word2 = word[:i] + '?' + word[i+1:]
			if word2 not in d:
				d[word2] = [word]
			else:
				d[word2].append(word)
	
	# populate adj
	for i in d:
		related = d[i]
		for a in range(len(related)):
			for b in range(len(related)):
				if a != b:
					adj[related[a]].append(related[b])
	return adj

def heuristic(w1, w2):
	similar = 0
	for i in range(len(w1)):
		if w1[i] == w2[i]:
			similar += 1
	return similar

def A_Star(graph, start, end):

    # determines whether there exists a path from start to end
    # graph is an adjacency list
	l = []					# queue l contains the current path
	heappush(l, (0, [start]))
	visited = set([start])		# set visited contains the visited vertices
	while l: # > 0
		# while l has elements		
		path = heappop(l)[1]
		# let path be the first path in l
		if path[-1] == end:
			# here, we have reached the end vertex, so return the path
			return path
		visited.add(path[-1])
		# if not, then add this particular path to visited
		
		# for each neighbor of the last vertex in the path,
		# add it to the path only if it has not been visited already
		for neighbor in graph[path[-1]]:
			if neighbor not in visited:
				heappush(l, (-heuristic(neighbor, end), path+[neighbor]))
	return -1 # if no path from start to end exists
f = open('6-letter-words.txt', 'r')
lines = f.readlines()
adjl = create_adjacency_list(lines)


graph = {1:[7], 2:[6], 3:[1, 5], 4:[6],
		 5:[2, 4], 6:[8], 7:[2, 8], 8:[]}













