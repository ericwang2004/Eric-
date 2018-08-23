# comment this
# runtime of insert, delete, minimum, heapsort
# table in google docs
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
		# runtime: O(log n)
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
		# runtime: O(log n)
		# first make last element the root and delete the original root
		self.elems[1] = self.elems[-1]
		del self.elems[-1]
		# push root element down the heap until heap property is satisfied
		i = 1
		while i <= len(self.elems)-1:
			# case 1: element has no children
			if 2*i > len(self.elems)-1:
				# heap property is satisfied
				return
			elif 2*i+1 > len(self.elems)-1:
				# case 2: element has a left child but no right child
				if self.elems[i] <= self.elems[2*i]:
					# check if element satisfies heap property
					return
				else: # if not, then swap the element with its left child
					self.elems[i], self.elems[2*i] = self.elems[2*i], self.elems[i]
					i *= 2			

			else: # case 3: element has left and right children
				left = self.elems[2*i]
				right = self.elems[2*i+1]
				if self.elems[i] <= min(left, right):
					# in this case, element satisfies heap property
					return
				# swap element with the smaller child
				if left < right:
					# swap with left
					self.elems[i], self.elems[2*i] = self.elems[2*i], self.elems[i]
					i = 2*i
				else: # swap with right
					self.elems[i], self.elems[2*i+1] = self.elems[2*i+1], self.elems[i]
					i = 2*i+1

	def minimum(self):
		# runtime: O(1)
		return self.elems[1]

def heapsort(l):
	# runtime: O(n log n)
	sort = []
	h = Heap()
	for x in l:
		# make the array l into a heap
		h.insert(x)
	while len(h.elems) > 1:
		# the root of the heap must be the minimum element
		sort.append(h.minimum())
		# each time delete the root and append the new minimum element
		h.delete()
	# return the list of sorted items
	return sort


h = Heap()
for i in range(7, 0, -1):
	h.insert(i)










