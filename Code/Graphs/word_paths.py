# comment this
# find the longest shortest path between two words
# runtime of BFS, DFS, create_adjacency_list
# DFS
#

from collections import deque



def BFS(graph, start, end):
    # determines whether there exists a path from start to end
    # graph is an adjacency list
	l = deque() 
	l.append([start])
	visited = set([start])
	while l: # > 0     
		path = l.popleft()
		if path[-1] == end:
			return path
		visited.add(path[-1])
		
		for neighbor in graph[path[-1]]:
			if neighbor not in visited:
				l.append(path + [neighbor])
	return -1

def connected(w1, w2):
	# check if w1 and w2 differ by exactly 1 letter
	# assume w1 an w2 are the same length
	difference = 0
	for i in range(len(w1)):
		if w1[i] != w2[i]:
			difference += 1
		if difference > 1:
			return False
	return True

def create_adjacency_list(lines):

	adj = {}
	d = {}
	for word in lines:
		word = word.strip()
		adj[word] = []
		for i in range(len(word)):
			word2 = word[:i] + '?' + word[i+1:]
			if word2 not in d:
				d[word2] = [word]
			else:
				d[word2].append(word)
	
	for i in d:
		related = d[i]
		for a in range(len(related)):
			for b in range(len(related)):
				if a != b:
					adj[related[a]].append(related[b])

	return adj

f = open('6-letter-words.txt', 'r')
lines = f.readlines()
adjl = create_adjacency_list(lines)
















