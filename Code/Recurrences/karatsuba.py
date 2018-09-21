#
#
#
#
#


def karatsuba(a, b):
	a_len = len(str(a))
	b_len = len(str(b))
	# a -> AB, b -> CD
	if a_len == 1 or b_len == 1:
		return a*b
	# 1. Split
	A = a//(10**(a_len//2))
	B = a%(10**(a_len//2))
	C = b//(10**(b_len//2))
	D = b%(10**(b_len//2))

	# 2. Determine AC, BD, (A+B)(C+D) - AC - BD
	x = karatsuba(A, C)
	y = karatsuba(B, D)
	z = karatsuba(A+B, C+D) - x - y

	product = x * 10**(a_len) + z * 10**(a_len//2) + y
	return product
	
	



