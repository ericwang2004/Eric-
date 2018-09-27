#
#
#
#
#





f = open('graph.txt', 'r')

adj_list = {}
element_list = []
adj_matrix = []
for line in f:
	# if it's a vertex
	if len(line) == 2:
		adj_list[line.strip('\n')] = []
		
		element_list.append(line[0]) # to keep track of row and column headings
		adj_matrix.append([]) # create new row at each new vertex
		for row in adj_matrix:
			while len(row) <= len(element_list)-1:
				row.append(0)
		# print(adj_matrix)

	# if it's an edge
	elif len(line) == 4:
		
		adj_list[line[0]].append(line[2])
		adj_matrix[element_list.index(line[0])][element_list.index(line[2])] = 1
		
#print(adj_list)
#print(adj_matrix)














