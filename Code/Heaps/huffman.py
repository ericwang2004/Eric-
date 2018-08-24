# 1. given a string, call get_frequencies to get a dictionary of letters and their frequencies
# 2. use a HuffmanNode class on each letter in the dictionary and insert all of them into a min-heap
# 3. take out the two smallest HuffmanNodes and combine those into one HuffmanNode - use a special character not present in the string
# 4. insert the new node into the heap
# 5. repeat steps 3 and 4 until only one node remains, which is the root of the Huffman tree
#
#

from heaps import Heap

@total_ordering
class HuffmanNode:

	def __init__(self, char, freq):
		self.char = char
		self.freq = freq
		self.left = 0
		self.right = 0

	def __ge__(self, other):
		return self.freq >= other.freq

	def __eq__(self, other):
		return self.freq == other.freq


def get_frequencies(string):
	letters = {}
	for c in string:
		if c in letters.




