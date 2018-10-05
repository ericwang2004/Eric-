#
#
#
#
# write a DFS version of exists path
# comment this

def exists_path_BFS(graph, start, end):
	# determines whether there exists a path from start to end
	# graph is an adjacency list
	l = [start]
	visited = set([start]) # list of visited vertices
	while len(l): # > 0
		for v in graph[l[0]]:
			if v == end:
				return True
			if v not in visited:
				l.append(v)
				visited.add(v)
		del l[0]
	return False	
		
graph = {1:[7], 2:[6], 3:[1, 5], 4:[6],
		 5:[2, 4], 6:[8], 7:[2, 8], 8:[]}







