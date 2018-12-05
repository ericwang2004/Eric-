#
#
#
#

from collections import deque

G = {'0':['1'], '1':['0','2'], '2':['1','3','6','7'],
	'3':['2','4'], '4':['3','5'], '5':['4'], '6':['2'],
	'7':['2','8'], '8':['7']}

def create_graph(G):
	# creates the graph of pairs of vertices
	v_pairs = {}
	for v1 in G:
		for v2 in G:
			if v1 != v2 and v2 not in G[v1]:
				# only include in the graph if they are not same or adjacent
				v_pairs[(v1, v2)] = []
	for p1 in v_pairs:
		# connect them if one can be obtained by the other in 1 unit of time
		for p2 in v_pairs:
			if p1 != p2:
				if p1 not in v_pairs[p2]:
					#print(p1, p2)
					if p1[0] in G[p2[0]] or p1[0] == p2[0]:
						if p1[1] in G[p2[1]] or p1[1] == p2[1]:
							v_pairs[p1].append(p2)
							v_pairs[p2].append(p1)
	return v_pairs

def BFS(G, start, end):
	l = deque()
	# l is a queue which will contain the current path
	l.append([start])
	visited = set([start])
	while l:
		path = l.popleft()
		if path[-1] == end: # in which case we reached the end
			return path
		visited.add(path[-1])
		for neighbor in G[path[-1]]:
			if neighbor not in visited:
				l.append(path + [neighbor])
	return -1

# Alice and Bob start at (0, 5) and end at (8, 6)
path = BFS(create_graph(G), ('0', '5'), ('8', '6'))
print(path)





