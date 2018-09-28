# 
# functions to create adj_list and adj_matrix
# 
# 
# 



def is_vertex(string):
	return ' ' not in string



f = open('graph.txt', 'r')
lines = f.readlines()

adj_list = {}
element_list = {}

count = 0
enc_edge = False

for line in lines:
	line = line.strip()
	# if it's a vertex
	if is_vertex(line):
		adj_list[line] = []
		
		element_list[line] = count  # to keep track of row and column headings
		count += 1
	# if it's an edge
	else:
		if not enc_edge:
			adj_matrix = [[] for i in range(count)] 
		
		v1, v2 = line.split(' ')		
		adj_list[v1].append(v2)
		adj_matrix[element_list[v1]][element_list[v2]] = 1
		
#print(adj_list)
#print(adj_matrix)


f.close()











