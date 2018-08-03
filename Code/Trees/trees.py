# for every function that can be written with 3 cases, write it with 3 cases
# comment code, summarize print_path_to and sum_path
# write equals method for node and tree class
# given a sorted array, write a function to return the index of an element in O(log n)

class BinaryTreeNode:

	# methods defined here:
	# is_leaf, count_nodes, count_leaves, contains, height, invert, is_full, minimum
	# preorder, inorder, postorder, maximum, print_path_to, sum_path_helper/sum_path
	
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
		elif self.right == 0 and self.left != 0: # if node only has left child
			return self.left.count_nodes() + 1 # count the nodes under left child and itself 
		elif self.right != 0 and self.left == 0: # similarly for only right child
			return self.right.count_nodes() + 1
		else:
			return self.left.count_nodes() + self.right.count_nodes() + 1
			# count the sum of nodes under both children including itself

	def count_leaves(self):
		if self.is_leaf():
			return 1
		elif self.right == 0 and self.left != 0: # if node only has left child
			return self.left.count_leaves() # count the number of leaves under left child
		elif self.right != 0 and self.left == 0: # similar for right child
			return self.right.count_leaves()
		else: # if it has both children, count the total number of leaves under both
			return self.left.count_leaves() + self.right.count_leaves()
			

	def contains(self, value):
		# checks if value is in the subtree
		if self.value == value:
			return True
		elif self.is_leaf(): # if node is leaf and node.value != value
			return False
		if self.left != 0: # if it has a left child, check if it contains value
			return self.left.contains(value)
		if self.right != 0: # similarly for right child
			return self.right.contains(value)

	def height(self):
		# returns number of levels
		# root is at level 0 but has height 1
		if self.is_leaf():
			return 1
		elif self.right == 0 and self.left != 0:
			return self.left.height() + 1 # this includes the current node
		elif self.right != 0 and self.left == 0:
			return self.right.height() + 1
		else: # self.right != 0 and self.left != 0
			return max(self.right.height(), self.left.height()) + 1
			# should return the greatest value from the set of path lengths from the current node to a leaf

	def invert(self):
		# swaps left and right children of every node
		if self.is_leaf():
			return
		self.right, self.left = self.left, self.right
		if self.left != 0:
			self.left.invert()
		if self.right != 0:
			self.right.invert()

	def is_full(self):
		# check if every node in the subtree has two or zero children
		if self.is_leaf():
			return True
		elif self.right == 0 or self.left == 0:
			# if either left or right is missing, tree cannot be full
			return False
		else:
			# if there is at least one false, then return false
			return self.right.is_full() and self.left.is_full()
	
	def minimum(self):
		# returns the minimum value of a node in the tree
		if self.is_leaf():
			return self.value
		elif self.right == 0 and self.left != 0:
			# compares value of current node to all those under its left child
			return min(self.left.minimum(), self.value)
		elif self.right != 0 and self.left == 0:
			# similarly for right child
			return min(self.right.minimum(), self.value)
		else: # compares current node value to those under both children, if both children exist
			return min(self.right.minimum(), self.left.minimum(), self.value)

	def preorder(self):
		# preorder: itself, left, right
		print(self.value)
		if self.left != 0:
			self.left.preorder()
		if self.right != 0:
			self.right.preorder()

	def inorder(self):
		# inorder: left itself, right
		if self.left != 0:
			self.left.inorder()
		print(self.value)
		if self.right != 0:
			self.right.inorder()

	def postorder(self):
		# postorder: left, right, itself
		if self.left != 0:
			self.left.postorder()
		if self.right != 0:
			self.right.postorder()
		print(self.value)
	
	def maximum(self):
		# returns the greatest value of a node in the tree
		# same as minimum, just replace .minimum with .maximum
		if self.is_leaf():
			return self.value
		elif self.right != 0 and self.left == 0:
			return max(self.right.maximum(), self.value)
		elif self.left != 0 and self.right == 0:
			return max(self.left.maximum(), self.value)
		else:
			return max(self.right.maximum(), self.left.maximum(), self.value)

	def print_path_to(self, value):
		'''
		This prints the path from the current node to the node containing the 
		specified value. 
		1. Check if the right subtree exists and if it contains the value
		2. Perform the same task for the left subtree
		3. Suppose descendant of right child contains value -- then repeat these steps on the right child
		4. If descendant of left child contains value, repeat these steps on the left child 
		'''
		# assuming value is actually in the tree
		print(self.value) # print the value of the current node
		if self.value == value:
			return
		if self.right != 0 and self.right.contains(value):
			# if subtree with root self.right contains the value, print path to value on the right child
			self.right.print_path_to(value)
		if self.left != 0 and self.left.contains(value):
			# similarly for left child
			self.left.print_path_to(value)


	def sum_path_helper(self, path):
		'''
		This prints all the path sums, where the sum of a path is the sum of all the values of the nodes
		on the path. The path variable stores the values of the nodes along the path. At each node, it will
		continue to the left or right child if they exist and append the value of the current node to path.
		This process continues until a leaf node is reached, in which case it will print the sum of all the 
		values stored in path and the leaf node. 
		'''
		if self.is_leaf():
			print(self.value+sum(path))
		if self.left != 0:
			self.left.sum_path_helper(path+[self.value])
		if self.right != 0:
			self.right.sum_path_helper(path+[self.value])

	def sum_path(self):	
		self.sum_path_helper([])

	def __eq__(self, other):
		'''
		# allows for comparison between two binary trees
		# two binary trees are equal if each node has the same left and right children
		
		if self.value != other.value:
			# if the values of the root nodes are not equal, then clearly the trees cannot be equal
			return False
		else: # if the values are equal
			if (self.is_leaf and not other.is_leaf) or (not self.is_leaf and other.is_leaf):
				# check if one is a leaf and the other isn't
				return False
			else: # if both are leaves
				return True # since their values are the same
		if self.right != 0 and other.right != 0 and self.right.value == other.right.value:
			return self.right.equals(other.right)
		if self.left != 0 and other.left != 0 and self.left.value == other.left.value:
			return self.left.equals(other.left)
		'''
		if type(self) != type(other):
			return False
		r = True
		if self.value != other.value:
			r = False

		if self.right == other.right == 0:
			r &= True
		elif self.right != 0 and other.right != 0:
			r &= self.right == other.right
		else:
			r = False
		
		if self.left == other.left == 0:
			r &= True
		elif self.left != 0 and other.left != 0:
			r &= self.left == other.left
		else:
			r = False
		
		return r

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
	
	def __eq__(self, other):
		return self.root == other.root

def combine(root, tree1, tree2):
	new_tree = BinaryTree(root)
	root.left = tree1.root
	root.right = tree2.root
	return new_tree


'''
l = [BinaryTreeNode(i) for i in range(32)]
l = [0] + l

bt = BinaryTree(l[1])
for i in range(1, 16):
	l[i].left = l[2*i]
	l[i].right = l[2*i+1]
'''

set1 = [BinaryTreeNode(i) for i in range(5)]
set1[0].right = set1[1]
set1[0].left = set1[2]
set1[2].left = set1[4]
set1[2].right = set1[3]
tree = BinaryTree(set1[0])

set2 = [BinaryTreeNode(i) for i in range(5)]
set2[0].right = set2[1]
set2[0].left = set2[2]
set2[2].left = set2[4]
set2[2].right = set2[3]
tree2 = BinaryTree(set2[0])
'''
			  0
		2		   1
	 4	   3  

'''










