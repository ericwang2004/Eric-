#
#
#
#
#



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
	for word in lines:
		adj[word] = []
	for word in lines:
		for key in adj:
			if connected(word, key):
				adj[key].append(word)
	return adj

def exists_word_path(w1, w2):
	# 6 letter words
	f = open('6-letter-words.txt', 'r')
	lines = f.readlines()
	adjl = create_adjacency_list(lines)
	
	return exists_path_BFS(adjl, w1, w2)
















