# 
# functions to create adj_list and adj_matrix
# 
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

def topological_sort(lines):
	adjm = adj_matrix(lines) # create adjacency matrix
	L = [] # L will contain the sorted vertices
	indices = {} # dict of index:vertex 
	v2edges = {} # dict of vertex:number of incoming edges	
	# 1. make indices
	# 2. simultaneously make keys of v2edges, setting number of incoming edges = 0
	# 3. use adjm to make values of v2edges
	
	# steps 1, 2
	count = 0
	for line in lines:
		line = line.strip()
		if ' ' in line: # ignore the edges
			break
		else: # we only need the vertices
			v2edges[line] = 0
			indices[count] = line
			count += 1

	# step 3, look down each column and count the number of 1s for each vertex
	for i in range(len(adjm[0])):
		for row in adjm:
			if row[i] == 1:
				v2edges[indices[i]] += 1
	
	A = [v for v in v2edges if v2edges[v]==0] # set of vertices with no incoming edges
	
	while len(A) > 0: # while A is not empty
		element = A.pop()
		L.append(element) # choose an element from A and transfer it into L
		# find all vertices adjacent to element and -1 from incoming edges
		# in adjm: change all 1s to 0s in element's row
		e_index = -1
		for i in indices:
			if indices[i] == element: # find index of element to locate it in adjm
				e_index = i
				break
		if e_index != -1:
			for j in range(len(adjm[e_index])): # change any 1s to 0s
				if adjm[e_index][j] == 1:
					# -1 from vertex with index j's incoming edges
					v2edges[indices[j]] -= 1
					adjm[e_index][j] = 0
		for vertex in v2edges:
			if v2edges[vertex] == 0 and vertex not in A and vertex not in L:
				A.append(vertex)

	return L

f = open('courses.txt', 'r')
lines = f.readlines()

print(topological_sort(lines))
		
		











