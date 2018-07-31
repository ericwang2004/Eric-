# for every function that can be written with 3 cases, write it with 3 cases
# comment code, summarize print_path_to and sum_path
# write equals method for node and tree class
# given a sorted array, write a function to return the index of an element in O(log n)

class BinaryTreeNode:

	def __init__(self, value):
		self.right = 0
		self.left = 0
		self.value = value

	def is_leaf(self):
		# node does not have any children
		return self.right == self.left == 0

	def count_nodes(self):
		# counts the number of nodes in subtree
		if self.is_leaf():
			return 1
		elif self.right == 0 and self.left != 0:
			return self.left.count_nodes() + 1
		elif self.right != 0 and self.left == 0:
			return self.right.count_nodes() + 1
		else:
			return self.left.count_nodes() + self.right.count_nodes() + 1

	def count_leaves(self):
		if self.is_leaf():
			return 1
		elif self.right == 0 and self.left != 0:
			return self.left.count_leaves()
		elif self.right != 0 and self.left == 0:
			return self.right.count_leaves()
		else:
			return self.left.count_leaves() + self.right.count_leaves()
			

	def contains(self, value):
		# checks if value is in the subtree
		if self.value == value:
			return True
		elif self.is_leaf(): # if node is leaf and node.value != value
			return False
		elif self.right == 0 and self.left != 0:
			return self.left.contains(value)
		elif self.left == 0 and self.right != 0:
			return self.right.contains(value)
		else: # if at least one node returns true then return true
			return self.right.contains(value) or self.left.contains(value)


	def height(self):
		# returns number of levels
		# root is at level 0 but has height 1
		if self.is_leaf():
			return 1
		elif self.right == 0 and self.left != 0:
			return self.left.height() + 1
		elif self.right != 0 and self.left == 0:
			return self.right.height() + 1
		else: # self.right != 0 and self.left != 0
			return max(self.right.height(), self.left.height()) + 1

	def invert(self):
		# swaps left and right children of every node
		if self.is_leaf():
			return
		elif self.right == 0 and self.left != 0:
			self.right = self.left
			self.left = 0
			self.right.invert()
		elif self.right != 0 and self.left == 0:
			self.left = self.right
			self.right = 0
			self.left.invert()
		else:
			self.right, self.left = self.left, self.right
			self.right.invert()
			self.left.invert()

	def is_full(self):
		# check if every node in the subtree has two or zero children
		if self.is_leaf():
			return True
		elif self.right == 0 or self.left == 0:
			return False
		else:
			return self.right.is_full() and self.left.is_full()
	
	def minimum(self):
		if self.is_leaf():
			return self.value
		elif self.right == 0 and self.left != 0:
			return min(self.left.minimum(), self.value)
		elif self.right != 0 and self.left == 0:
			return min(self.right.minimum(), self.value)
		else:
			return min(self.right.minimum(), self.left.minimum(), self.value)

	def preorder(self):
		print(self.value)
		if self.left != 0:
			self.left.preorder()
		if self.right != 0:
			self.right.preorder()

	def inorder(self):
		if self.left != 0:
			self.left.inorder()
		print(self.value)
		if self.right != 0:
			self.right.inorder()

	def postorder(self):
		if self.left != 0:
			self.left.postorder()
		if self.right != 0:
			self.right.postorder()
		print(self.value)
# preorder: itself, left, right
# inorder: left, itself, right 4, 2, 5, 3, 6, 0, 1
# postorder: left, right, itself 4, 5, 6, 3, 2, 1, 0
	
	def maximum(self):
		if self.is_leaf():
			return self.value
		elif self.right != 0 and self.left == 0:
			return max(self.right.maximum(), self.value)
		elif self.left != 0 and self.right == 0:
			return max(self.left.maximum(), self.value)
		else:
			return max(self.right.maximum(), self.left.maximum(), self.value)

	def print_path_to(self, value):
		print(self.value)
		if self.value == value:
			return
		elif self.right == 0 and self.left != 0:
			self.left.print_path_to(value)
		elif self.right != 0 and self.left == 0:
			self.right.print_path_to(value)
		else:
			if self.right.contains(value):
				self.right.print_path_to(value)
			elif self.left.contains(value):
				self.left.print_path_to(value)

	def sum_path_helper(self, path):
		if self.is_leaf():
			print(self.value+sum(path))
		if self.left != 0:
			self.left.sum_path_helper(path+[self.value])
		if self.right != 0:
			self.right.sum_path_helper(path+[self.value])

	def sum_path(self):	
		self.sum_path_helper([])


class BinaryTree:

	def __init__(self, root):
		self.root = root

	def count_nodes(self):
		return self.root.count_nodes()

	def count_leaves(self):
		return self.root.count_leaves()

	def contains(self, value):
		return self.root.contains(value)

	def height(self):
		return self.root.height()

	def invert(self):
		return self.root.invert()

	def is_full(self):
		return self.root.is_full()
	
	def minimum(self):
		return self.root.minimum()

	def preorder(self):
		self.root.preorder()

	def inorder(self):
		self.root.inorder()

	def postorder(self):
		self.root.postorder()

	def maximum(self):
		return self.root.maximum()

	def print_path_to(self, value):
		self.root.print_path_to(value)

	def sum_path(self):
		self.root.sum_path()

def combine(root, tree1, tree2):
	new_tree = BinaryTree(root)
	root.left = tree1.root
	root.right = tree2.root
	return new_tree



l = [BinaryTreeNode(i) for i in range(32)]
l = [0] + l

bt = BinaryTree(l[1])
for i in range(1, 16):
	l[i].left = l[2*i]
	l[i].right = l[2*i+1]




'''
			  0
		2		   1
	 4	   3  

'''










