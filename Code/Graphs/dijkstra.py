# Dijkstra
#
#
#
#

class infinity(float):
	def __gt__(self, other):
		return True
	def __lt__(self, other):
		return False

def create_adjacency_list(lines):
	adjl = {}
	for line in lines:
		line = line.strip()
		if ' ' not in line: # it's a vertex
			adjl[line] = []
		else: # it's an edge
			v1, v2, w = line.split(' ')
			adjl[v1].append((v2, float(w)))
	return adjl

def dijkstra(graph, start):
	# graph adjacency list
	unvisited = []
	distances = {}
	previous = {}
	current = start

	for v in graph:
		unvisited.append(v[0])
		previous[v[0]] = None
		# set initial distances
		if v == start:
			# distance to start is 0
			distances[v[0]] = 0
		else:
			# distance to every other vertex is infinity
			distances[v[0]] = infinity()

	while True:
		# consider all neighbors of the current node
		for neighbor in graph[current]:
		
			# calculate the tentative distance from start to neighbor
			# = distance from start to current + distance from current to neighbor
				
			for x in graph[current]:
				# find distance from current to neighbor
				if x[0] == neighbor[0]:
					current2neighbor = x[1]

			tentative_distance = distances[current] + current2neighbor
			# compare tentative distance and the originally assigned distance
			if tentative_distance < distances[neighbor[0]]:
				distances[neighbor[0]] = tentative_distance
				previous[neighbor[0]] = current	
	
		# remove current from unvisited when done considering neighbors
		unvisited.remove(current)
		
		if len(unvisited) == 0:
			# if there are no more vertices to be checked, break loop
			break
		else: # set current = unvisited node with smallest distance
			current = unvisited[0]
	
	return distances, previous

f = open('dijkstra_graph.txt', 'r')
lines = f.readlines()
f.close()

G = create_adjacency_list(lines)
print(dijkstra(G, 'A'))




