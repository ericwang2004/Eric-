import math
import random
import sys

sys.setrecursionlimit(1000000)
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
letter_index = {} # {a:1, b:2, ...}
for i in range(26):
	letter_index[letters[i]] = i+1
index_letter = {} # {1:a, 2:b, ...}
for i in range(26):
	index_letter[i+1] = letters[i]

def divisible(a, b):
	return not a % b

def is_prime(p):
	primes = primes_upto(math.floor(math.sqrt(p))) 
	for q in primes:
		if p % q == 0:
			return False
	return True

def primes_upto(limit):
	# O(n log(log(n)))
	# generate a list of primes less than or equal to limit
	A = [False, False] # boolean array: true if prime, false if composite
	primes = [] # will store the primes
	A += [True]*(limit-1)
	for i in range(2, math.ceil(math.sqrt(limit))):
		if A[i]:
			for j in range(i**2, limit+1, i):
				# i**2, i**2+i, ..., not exceeding n
				A[j] = False
	return list(i for i in range(len(A)) if A[i])

def factor(n):
	primes = primes_upto(n)
	factors = []
	while n > 1:
		for p in primes:
			if n % p == 0:
				factors.append(p)
				n /= p
				break
	return factors

def gcd(a, b):
	if a == 0 or b == 0:
		return abs(a-b)
	if a >= b:
		return gcd(a % b, b)
	else:
		return gcd(a, b % a)

def egcd(a, b):
	# returns (g, x, y) such that g = ax + by
	if b == 0:
		# g = (a, 0) = a, a*1+b*0 = a
		return (a, 1, 0)
	g1, x1, y1 = egcd(b, a % b)
	return (g1, y1, x1-(a//b)*y1)

def modular_inverse(a, n):
	#for i in range(2, limit+1):
	#	A.append(True)
	# x such that ax = 1 mod n
	# => ax + (-b)n = gcd(a, n) = 1
	# => x = egcd(a, n)[1]
	return egcd(a, n)[1]%n

def modular_exponentiation(a, b, n):
	# a**b mod n
	a %= n
	if b == 1:
		return a
	if b % 2 == 0:
		# a**(2k) = (a**2)**k
		return modular_exponentiation(a**2 % n, b//2, n) % n
	else:
		# a**(2k+1) = a*(a**2)**k, 2k+1 = b => k = (b-1)//2
		return a*modular_exponentiation(a**2 % n, (b-1)//2, n) % n

def totient(N, primes):
	# totient of N with list of distinct primes dividing it
	phi = N
	for p in primes:
		phi *= 1-1/p
	return phi

def generate_prime(bitsize):
	# generate prime of bitsize bits
	p = random.randrange(2**(bitsize-1), 2**bitsize)
	while not miller_rabin(p):
		p = random.randrange(2**(bitsize-1), 2**bitsize)
	return p

def generate_keys(bitsize):
	# ( (N, e), (p, q, d) )
	p = generate_prime(bitsize)
	q = generate_prime(bitsize)
	N = p*q
	e = 3
	phi = (p-1)*(q-1)
	d = modular_inverse(e, phi)
	return ((N, e), (p, q, d)) # (public, private)

def message_to_int(m):
	# assume message consists solely of lowercase letters
	# convert to base 26
	n = 0
	for i in range(len(m)):
		n += letter_index[m[len(m)-i-1]] * (26**i)
	return n
		
def int_to_message(n):
	m = ""
	place = math.floor(math.log(n, 26))
	while place >= 0:
		digit = n // (26**place)
		m += index_letter[digit]
		n -= digit*(26**place)
		place -= 1
	return m

def encrypt(public_key, message):
	# message**e mod N
	# public_key = (N, e)
	N, e = public_key
	return modular_exponentiation(message, e, N)

def decrypt(private_key, encrypted_message):
	# encrypted_message**d mod N (N = p*q)
	# private_key = (p, q, d)
	p, q, d = private_key
	return modular_exponentiation(encrypted_message, d, p*q)

def crack(public_key, encrypted_message):
	# decrypt the encrypted message given the public key
	N, e = public_key
	p, q = factor(N) # p*q = N = public_key[0]
	d = modular_inverse(e, (p-1)*(q-1))
	private_key = (p, q, d)
	return decrypt(private_key, encrypted_message)

def witness(a, n, t, u):
	x_0 = modular_exponentiation(a, u, n)
	x_1 = x_0**2 % n
	for _ in range(t):
		x_1 = x_0**2 % n
		if x_1 == 1 and x_0 != 1 and x_0 != n-1: # try to find nontrivial sqrt(1)
			return True # (..., d, 1, ...) nontrivial root at d found
		x_0 = x_1
	if x_1 != 1:
		return True # fermat primality test, it is composite
	return False

def miller_rabin(n, trials=40):
	# write n-1 = 2**t*u
	t = 0
	u = n-1
	while u % 2 == 0:
		u //= 2
		t += 1
	for i in range(trials):
		a = random.randrange(1, n)
		if witness(a, n, t, u):
			return False # composite
	return True # prime

def primitive_root(p):
	# p != 2 is prime, compute a primitive root g
	found = False
	while not found:
		g = random.randrange(2, p-1) # because g != 1 or p-1
		# now test if g is a primitive root by considering d = ord_p(g)
		# d|p-1
		for d in set(factor(p-1)):
			if d != p-1:
				# make sure g**d != 1 (mod p)
				if modular_exponentiation(g, d, p) == 1:
					break
			found = True
		if found:
			break
	return g
	
def diffie_hellman(p):
	g = primitive_root(p)
	print("g={}".format(g))
	A = random.randrange(100, 200)
	B = random.randrange(100, 200)
	print("A={}, B={}".format(A, B))
	print("A sends {} to B".format(modular_exponentiation(g, B, p)))
	print("B sends {} to A".format(modular_exponentiation(g, A, p)))
	print("The secret key is {}".format(modular_exponentiation(g, A*B, p)))

def brute_force(g, a, p):
	prod = 1
	for i in range(1, p):
		prod *= g
		prod %= p
		if prod == a:
			return i

def baby_step_giant_step(g, a, p):
	d = {}
	m = math.ceil(math.sqrt(p))
	G = modular_inverse(modular_exponentiation(g, m, p), p)
	A = a
	prod = 1
	for j in range(1, m):
		prod = prod*g%p
		if prod == a:
			return j
		d[prod] = j
	i = 0
	while True:
		if A in d:
			j = d[A]
			break
		A *= G
		A %= p
		i += 1
	return i*m+j	
	
def chinese_remainder_theorem(rems, mods):
	'''
	rems = {a_1,...,a_n}
	mods = {m_1,...,m_n}, M = m_1*...*m_n, 
	find x (reduced on mod M) : x = a_i (mod m_i) for i=1,...,n
	'''
	# m_i pairwise coprime => gcd(M/m_i, m_i)=1
	# there exists b_i with (M/m_i)*b_i = 1 (mod m_i)
	# multiply by a_i to get (M/m_i)*b_i*a_i = a_i (mod m_i) for all i
	n = len(rems)
	M = 1
	for i in range(n):
		M *= mods[i]
	# x = sum_{i=1}^{n} (M/m_i)*b_i*a_i solves the system
	x = 0
	for i in range(n):
		b_i = modular_inverse(M//mods[i], mods[i])
		x += M//mods[i]*b_i*rems[i]
		x %= M
	return x

def pohlig_hellman(g, a, p, factors):
	'''
	find x such that g^x = a (mod p)
	'''
	pass











	









	
