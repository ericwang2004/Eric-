# 1. given a string, call get_frequencies to get a dictionary of letters and their frequencies
# 2. use a HuffmanNode class on each letter in the dictionary and insert all of them into a min-heap
# 3. take out the two smallest HuffmanNodes and combine those into one HuffmanNode - use a special character not present in the string
# 4. insert the new node into the heap
# 5. repeat steps 3 and 4 until only one node remains, which is the root of the Huffman tree
#
#

from heaps import Heap


class HuffmanNode:

	def __init__(self, char, freq):
		self.char = char
		self.freq = freq
		self.left = 0
		self.right = 0

	def is_leaf(self):
		return self.char != 'special character'
	
	def contains(self, character):
		# check if subtree contains character
		# we need this for trace_path_to method
		if self.char == character:
			return True
		elif self.is_leaf():
			return False
		if self.left != 0 and self.right == 0:
			return self.left.contains(character)
		if self.left == 0 and self.right != 0:
			return self.right.contains(character)
		if self.left != 0 and self.right != 0:
			return self.left.contains(character) or self.right.contains(character)

	def trace_path_to(self, character):
		# determines the encoding of a character
		code = '' # binary sequence
		pointer = self
		while pointer.char != character:
			if pointer.left.contains(character):
				code += '0'
				pointer = pointer.left
			else:
				code += '1'
				pointer = pointer.right
		return code

class HuffmanTree:

	def __init__(self, root):
		self.root = root
		self.value = self.root.freq
	
	def __ge__(self, other):
		return self.value >= other.value

	def __gt__(self, other):
		return self.value > other.value
	
	def __eq__(self, other):
		return self.value == other.value
	
	def contains(self, character):
		return self.root.contains(character)
	
	def trace_path_to(self, character):
		return self.root.trace_path_to(character)			

def combine(t1, t2):
	# creates a new tree with root r with left and right descendants t1 and t2, resp. 
	r = HuffmanNode('special character', t1.root.freq + t2.root.freq)
	new_tree = HuffmanTree(r)
	r.left = t1.root
	r.right = t2.root
	return new_tree

def get_frequencies(string):
	# given a string, return a dictionary of the frequencies of every characterr
	letters = {}
	for c in string:
		if c in letters.keys():
			letters[c] += 1
		else:
			letters[c] = 1
	# {letter:frequency}
	return letters

def construct_tree(freqs):
	# constructs the tree given the frequencies of each character
	nodes = [HuffmanNode(letter, freqs[letter]) for letter in freqs]
	# nodes contains the HuffmanNodes
	trees = [HuffmanTree(node) for node in nodes]
	h = Heap()
	for tree in trees:
		h.insert(tree) # the heap contains all the trees
	while len(h.elems) > 2: # including 0
		t1 = h.minimum() # extract the two least frequent letters
		h.delete()
		t2 = h.minimum()
		h.delete()
		newTree = combine(t1, t2) # create a new tree combining the two nodes
		h.insert(newTree) # insert the new tree back into the heap
	# at this point, the heap contains only one element
	return h.minimum()	

def encode_helper(current_node, current_bin, char_dict):
	if current_node.is_leaf(): # if the current node is a leaf
		char_dict[current_node.char] = current_bin # update char_dict
	if current_node.left != 0: # if the left node exists
		encode_helper(current_node.left, current_bin+'0', char_dict)
		# add 1 to the current binary path
	if current_node.right != 0: # same for right
		encode_helper(current_node.right, current_bin+'1', char_dict)
	
def encode(string):
	tree = construct_tree(get_frequencies(string))
	codes = {} # dictionary of encoded characters
	encode_helper(tree.root, '', codes)
	return codes

def decode(bin_seq, tree):
	# decode a given binary sequence
	pointer = tree.root
	text = ''
	for bit in bin_seq:
		if bit == '0': # go left
			pointer = pointer.left
		else: # go right
			pointer = pointer.right
		if pointer.is_leaf(): # if we've arrived at a leaf
			text += pointer.char # then update text
			pointer = tree.root # and reset the position of pointer
	return text











