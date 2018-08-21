# create heaps class, constructor, insert method
#
#
#
#


'''
					9
			5				3
		1				


l = [0, 23, 11, 9, 1, 5, 3]

'''


class Heap:
	
	# min heap - parent is smaller than children
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
			if self.elems[i] >= self.elems[i//2]:
				return
			else: # heap property not satisfied
				# swap them
				self.elems[i], self.elems[i//2] = self.elems[i//2], self.elems[i]
				i //= 2
	
	def delete(self):
		self.elems[1] = self.elems[-1]
		del self.elems[-1]
		i = 1
		while i <= len(self.elems)-1:
			if 2*i > len(self.elems)-1:
				return
			elif 2*i+1 > len(self.elems)-1:
				if self.elems[i] <= self.elems[2*i]:
					return
				else:
					self.elems[i], self.elems[2*i] = self.elems[2*i], self.elems[i]
					i *= 2			

			else:
				left = self.elems[2*i]
				right = self.elems[2*i+1]
				if self.elems[i] <= min(left, right):
					return
			
				if left < right:
					self.elems[i], self.elems[2*i] = self.elems[2*i], self.elems[i]
					i = 2*i
				else:
					self.elems[i], self.elems[2*i+1] = self.elems[2*i+1], self.elems[i]
					i = 2*i+1

	def minimum(self):
		return self.elems[1]

def heapsort(l):
	sort = []
	h = Heap()
	for x in l:
		h.insert(x)
	while len(h.elems) > 1:
		sort.append(h.minimum())
		h.delete()
	return sort


h = Heap()
for i in range(7, 0, -1):
	h.insert(i)















































