#
#
#
#
#


def karatsuba(a, b):
	if b > a:
		a, b = b, a
	a_len = len(str(a))
	b_len = len(str(b))	
	#print(a, b, a_len, b_len)	
	# a -> AB, b -> CD
	if a_len == 1 or b_len == 1:
		#print(a*b)
		return a*b
	# 1. Split
	shift = 10**(a_len//2)
	A = a//shift
	B = a%shift
	C = b//shift
	D = b%shift

	# 2. Determine AC, BD, (A+B)(C+D) - AC - BD
	x = karatsuba(A, C)
	y = karatsuba(B, D)
	z = karatsuba(A+B, C+D) - x - y

	product = x * 10**(a_len//2*2) + z*shift + y
	#print(product)
	return product
	
	



