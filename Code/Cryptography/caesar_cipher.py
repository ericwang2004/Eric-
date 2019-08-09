
letters = "abcdefghijklmnopqrstuvwxyz"
alphabet1 = {} # index to letter
alphabet2 = {} # letter to index
i = 0
for l in letters:
	alphabet1[i] = l
	alphabet2[l] = i
	i += 1

def encrypt(message, shift):
	encrypted = ""
	for char in message:
		encrypted += alphabet1[(shift + alphabet2[char])%26]
	return encrypted

def decrypt(message, shift):
	decrypted = ""
	for char in message:
		decrypted += alphabet1[(alphabet2[char] - shift)%26]
	return decrypted

def crack(message):
	for shift in range(26):
		print(decrypt(message, shift))



