#
#
#


def and_(p, q):
	return not ((not p) | (not q))

def multiply(n):
	# multiply n by 5/8
	n = (n<<2) + n # multiply by 4 then add another n
	n >>= 3 # divide by 8
	return n
