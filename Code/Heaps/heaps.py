# create heaps class, constructor, insert method
#
#
#
#


class Heap:
	
	# max heap - parent is greater than children
	def __init__(self):
		self.elems = [0]
		'''
		root = second item in self.elems
		for every node at index i,
			left child is at index 2i
			right child is at index 2i + 1
		'''

	def insert(self, item):
		self.elems.append(item)
		i = len(self.elems)-1 # index of item
		while i//2 != 0:
			if self.elems[i] <= self.elems[i//2]:
				return
			else: # heap property not satisfied
				# swap them
				self.elems[i], self.elems[i//2] = self.elems[i//2], self.elems[i]
				i //= 2
		

	
h = Heap()
for i in range(1, 8):
	h.insert(i)















































