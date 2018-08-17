#
#
#


def and_(p, q):
	return not ((not p) | (not q))

def multiply(n):
	# multiply n by 5/8
	m = n & 7 # 7 = 0b 111, keep the shifted out bits
	n = n>>3 # divide by 8
	n = (n << 2) + n # multiply by 4 then add another n
	m = m>>3
	m = (m<<2)+m
	print(n, m)
