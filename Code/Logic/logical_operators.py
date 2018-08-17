#
#
# given a decimal number, write it in 8-bit two's complement
# count the number of 1's in binary representation
# make heap class
# 	in constructor, use list with leading 0, no arguments
# write insert method


'''
					23
			11				9
		1		5		3


l = [0, 23, 11, 9, 1, 5, 3]
'''


def and_(p, q):
	return not ((not p) | (not q))

def multiply(n):
	# multiply n by 5/8
	n = (n<<2) + n # multiply by 4 then add another n
	n >>= 3 # divide by 8
	return n
