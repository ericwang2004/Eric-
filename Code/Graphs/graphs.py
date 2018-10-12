# 
# functions to create adj_list and adj_matrix
# comment this
# 
# 

'''
parse text files:

f = open('textfile.txt', 'r')
lines = f.readlines()
for line in lines:
	...
	
'''

def adj_list(lines):
	# create adjacency list for graph
	adj_list = {}
	for line in lines:
		line = line.strip()
		if ' ' not in line:				# if its a vertex,
			adj_list[line] = []			# then create a new key in the list.
		else:							# if its an edge,
			v1, v2 = line.split(' ')	# append the other vertex in the edge to the
			adj_list[v1].append(v2)		# list of adjacent vertices.
	return adj_list

def adj_matrix(lines):
	element_list = {}	# dict of vertex:index
	count = 0
	edged = False # whether we have parsed all the vertices
	for line in lines:
		line = line.strip()
		if ' ' not in line: # if its a vertex, new key in element_list
			element_list[line] = count
			count += 1
		else:
			if not edged: # once finished with vertices, create the empty matrix
				adj_matrix = [[' ' for i in range(count)] for i in range(count)]
				edged = True
			v1, v2 = line.split(' ') # insert the 1s into the correct indices
			adj_matrix[element_list[v1]][element_list[v2]] = 1
	return adj_matrix

def topological_sort(adjlist):
	'''
	Procedure

	list L will contain the sorted vertices
	dict v2edges will contain the {vertices:number of incoming edges}
	list A will be the vertices with no incoming edges

	while A is not empty
		remove element from A and append it to L
		subtract 1 from the number of incoming edges to element
		append to A the new vertices now with 0 incoming edges

	return L
	'''
	L = []			# will contain the sorted vertices
	v2edges = {} 	# dictionary of vertices:number of incoming edges
	# 64-68 populate v2edges
	for vertex in adjlist: 		# create keys (vertices) of v2edges
		v2edges[vertex] = 0		# set initial value to 0
	for vertex in adjlist:		# create values
		for connection in adjlist[vertex]:
			v2edges[connection] += 1
	# 70 intialize A = set of vertices with 0 incoming edges
	A = [v for v in v2edges if v2edges[v]==0]

	while len(A) > 0:		# while A has elements
		element = A.pop()	# remove some element from A
		L.append(element)	# and append it to L
		# 76-79 subtract 1 from the number of incoming edges to element
		for v in adjlist[element]: # and append to A the new vertices
			v2edges[v] -= 1
			if v2edges[v] == 0:
				A.append(v2edges[v])
	
	return L

# write a DFS version of exists path
# comment this

def exists_path_BFS(graph, start, end):
	# determines whether there exists a path from start to end
	# graph is an adjacency list
	l = [start] # l is a queue: appends on the end, dels from the beginning
	visited = set([start]) # list of visited vertices
	while len(l): # > 0				# while l is not empty
		for v in graph[l[0]]:		# look through all vertices adjacent to l[0]
			if v == end:			# if it happens to be the end, there must be a path
				return True			
			if v not in visited:	# only append it to l if not already visited
				l.append(v)			# this way, we end when l is empty
				visited.add(v)		# implying there are no new vertices to be visited
		del l[0]
	return False

def exists_path_DFS(graph, start, end):
	l = [start]
	visited = set()
	while len(l):			
		for v in graph[l[0]]:	
			if v == end:		
				return True
			if v not in visited:
				l = [v] + l	
				visited.add(v)
		l.pop()
	return False

graph = {1:[7], 2:[6], 3:[1, 5], 4:[6],
		 5:[2, 4], 6:[8], 7:[2, 8], 8:[]}







