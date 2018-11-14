#
#
#
#
# Picture of G in google doc
G = {'A': [('B', 4.0), ('H', 8.0)], 'B': [('A', 4.0), ('C', 8.0)], 'C': [('B', 8.0), ('D', 7.0), ('F', 4.0), ('I', 2.0)], 'D': [('C', 7.0), ('E', 9.0), ('F', 14.0)], 'E': [('D', 9.0), ('F', 10.0)], 'F': [('C', 4.0), ('D', 14.0), ('E', 10.0), ('G', 10.0)], 'G': [('F', 2.0), ('H', 1.0), ('I', 6.0)], 'H': [('A', 8.0), ('B', 11.0), ('G', 1.0), ('I', 7.0)], 'I': [('C', 2.0), ('G', 6.0), ('H', 7.0)]}

# use dictionary to implement disjoint set
disjoint_sets = {} # vertex : parent

def make_set(v):
	disjoint_sets[v] = v

def find(v):
	# returns the root of v
	if disjoint_sets[v] != v:
		# along the way, we make every visited vertex's parent the root directly
		disjoint_sets[v] = find(disjoint_sets[v])
	return disjoint_sets[v]

def union(u, v):
	# make the root of v the parent of the root of u
	v_root = find(v)
	u_root = find(u)
	disjoint_sets[u_root] = v_root

def sort_edges(graph):
	# returns a list of edges in increasing weight order
	# graph is an adjacency list
	E = []
	for v1 in graph:
		for v2 in graph[v1]:
			if (v1, v2[0], v2[1]) != E not in E and (v2[0], v1, v2[1]) not in E:
				E.append((v1, v2[0], v2[1]))		
	return sorted(E, key=lambda x: x[2])

def MST_kruskal(graph):
	mst = [] # this will contain the edges of the mst
	for v in graph:
		# initially, make each vertex its own disjoint set
		make_set(v)
	# now, sort the edges by increasing weight
	edges = sort_edges(graph)	
	for e in edges:
		# e is a tuple of vertices (v1, v2)
		if find(e[0]) != find(e[1]):
			# then they will not form a cycle
			mst.append(e) # so add to mst
			union(e[0], e[1]) # and connect them
	return mst



