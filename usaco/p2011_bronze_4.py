#
#
#
# 2011 bronze 4

from collections import deque

def pageant(region1, region2):
	# regions are lists of coordinates
	l = deque()
	l.append(region1)
	visited = set(region1)
	while l:
		path = l.popleft()
		if path[-1] in region2:
			painted = []
			for point in path:
				if point not in region1 and  point not in region2:
					painted.append(point)
			return painted
		visited.add(path[-1])
		for x in [-1, 0, 1]:
			for y in [-1, 0, 1]:
				if abs(x) != abs(y):
					neighbor = (path[-1][0]+x, path[-1][1]+y)
					if neighbor not in visited:
						l.append(path + [neighbor])
	return -1

region1 = [(1,2),(2,2),(2,4),(3,2),(3,3),(3,4),(4,2),(4,3),(4,4),(5,3),(5,6),(6,3)]
region2 = [(8,1),(9,0),(9,1),(10,0),(10,1),(10,4),(11,0),(11,1),(11,2),(11,3),(11,4),
			(12,1),(12,2),(12,3),(12,4),(13,2)]


