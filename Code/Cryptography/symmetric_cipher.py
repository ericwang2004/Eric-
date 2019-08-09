import random
import collections

# in order of most to least common
letters = ['e', 't', 'a', 'o', 'h', 'n', 'i', 's', 'r', 'd', 'l', 'u', 'w', 'm', 'c', 'g', 'f', 'y', 'p', 'v', 'k', 'b', 'j', 'x', 'z', 'q']

def encrypt(message, key_map):
	# key_map = {A:H, B:R, ...}
	enc = ""
	for i in range(len(message)):
		char = message[i]
		enc += key_map[char] if char in letters else char
	"""
		if char in letters:
			enc += key_map[char]
		else:
			enc += char # for punctuation, which remains the same
	"""	
	return enc

def random_encrypt(message):
	# encrypt the message with random key_map
	shuffled = random.sample(letters, len(letters))
	key_map = {}
	for i in range(26):
		key_map[letters[i]] = shuffled[i]
	return encrypt(message, key_map)	

def decrypt(message, key_map):
	inv_map = {key_map[l]:l for l in key_map}
	# construct the inverse map
	return encrypt(message, inv_map)


def crack(message):
	# crack the message
	# freq = collections.Counter(message)
	freq = {} # frequency of letters in the encrypted message
	for char in message:
		if char in letters:
			if char not in freq:
				freq[char] = 1
			else:
				freq[char] += 1
	msg_letters = sorted(freq, key=lambda k: freq[k], reverse=True) # sort letters by frequency
	key_map = {} # construct key_map by matching msg_letters[] with letters[]
	# key_map: msg_letters --> letters
	for i in range(26):
		key_map[msg_letters[i]] = letters[i]
	print(key_map)
	return encrypt(message, key_map)

fin = open("harry_potter1.txt", "r")
lines = fin.readlines()
message = random_encrypt("".join(lines))
fin.close()

print(crack(message))


	
