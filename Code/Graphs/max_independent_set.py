

def push(graph, vertex, not_available, depth):
	#print(not_available)

	# make a tree of all "paths" of permissible permutations of V that satisfy the independent set property
	# find the maximum length path in the tree
	# at each step, we maintain the set of unavailable vertices
	for v in graph[vertex]:
		not_available.add(v)
	not_available.add(vertex)
	if len(not_available) == len(graph): # if everything is not available
		return depth # base case
	max_depth = 0
	for v in graph:
		if v not in not_available: # if v is available
			new_depth = push(graph, v, not_available, depth+1)
			if new_depth > max_depth:
				max_depth = new_depth
	return max_depth

def max_independent_set(graph):
	#for v in graph:
	#	r = root_node.add_child(v)
	#	push(graph, v, r)
	return max(push(graph, v, set(), 1) for v in graph)
	
G = {'A':['B','C'], 'B':['A','C','D','E'], 'C':['A','B','F','G'], 'D':['B','H'], 'E':['B','F'], 'F':['C','E','G'], 'G':['C','F','H','I'], 'H':['D','G','I'], 'I':['H','G']}
print(max_independent_set(G))

	
