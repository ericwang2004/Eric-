#
#
#
#
#


def multiply(m1, m2):
	# the number of columns of m1 = number of rows of m2
	if len(m1[0]) != len(m2):
		return []
	# result = rows of first x columns of second
	product_rows = len(m1)
	product_cols = len(m2[0])
	product = [[0 for i in range(product_cols)] for j in range(product_rows)]
	# for each row in m1
	for rows_m1 in range(len(m1)):
		# for each column in m2
		for cols_m2 in range(len(m2[0])): # the number of columns is the number of elements in any row
			# for each row in m2
			for rows_m2 in range(len(m2)):
				# we modify an element in product until the row of m1 changes or column of m2 changes
				product[rows_m1][cols_m2] += m1[rows_m1][rows_m2]*m2[rows_m2][cols_m2]
	return product

def split(m):
	# split step for matrices
	pass

def strassen_multiply(m1, m2):
	# assume each is square with power of 2 dimensions
	if len(m1) == 1:
		return [[m1[0][0] * m2[0][0]]]
	A1 = [[] for i in range()]	






m1 = [[1, 2, 3], [4, 5, 6]]
m2 = [[7, 8], [9, 10], [11, 12]]
#print(multiply(m1, m2, [[0, 0], [0, 0]]))



