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

def twos_complement(n):
	if n >= 0:
		b = bin(n)[2:]
		return '0b' + '0'*(8-len(b)) + b
	
	else: # negative numbers
		b = bin(-n)[2:]
		# binary representation of |n|
		bits = list(b)
		# invert the bits
		for i in range(len(bits)):
			if bits[i] == '1':
				bits[i] = '0'
			else:
				bits[i] = '1'
		# add 1
		if bits[-1] == '0':
			bits[-1] = '1'
		else:
			j = len(bits)-1
			while True:
				if bits[j] == '1':
					bits[j] = '0'
				if bits[j-1] == '0':
					bits[j-1] = '1'
					break
				j -= 1
		return '0b' + '1'*(8-len(bits)) + ''.join(bits)
	
def count_setbits(n):
	count = 0
	while n:
		if n & 1:
			count += 1
		n >>= 1
	return count






	
