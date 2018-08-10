# Comment this
# write a delete method
# runtime of insert, delete, and contains



'''

					10
			9				17
		5				12		23
	  3	  8			  11  13  20  37

'''

import trees

class BSTnode(trees.BinaryTreeNode):
	
	def __init__(self, value):
		super().__init__(value)

	def contains(self, number):
		# check if the BST contains this number
		if self.value == number:
			# if the node itself has value number, then the tree clearly contains number
			return True 
		if self.is_leaf():
			# if the node is a leaf and does not have value number,
			# then the tree does not contain number
			return False
		elif self.value > number:
			# if the node's value is greater than number,
			# then the number could be among the left descendants
			if self.left != 0:
				return self.left.contains(number)
			else:
				return False
		else:
			if self.right != 0:
				return self.right.contains(number)
			else:
				return False			

	def __repr__(self):
		 return "{} [{}, {}]".format(self.value, self.left, self.right)

class BST(trees.BinaryTree):
	
	def __init__(self, root):
		super().__init__(root)

	def contains(self, number):
		return self.root.contains(number)

	def insert(self, number):
		# inserts a number into the BST
		node = self.root # set the current node to self.root
		while True:
			if node.value == number:
				# if the number is already in the tree, then do nothing
				break
			elif node.value < number:
				# if the number is greater than the current node value,
				# then it must be stored on the right
				if node.right == 0:
					# if node.right does not exist, then a node containing number
					# can be stored there
					node.right = BSTnode(number)
					break
				else: # otherwise, set the current node to node.right,
					# and eventually find a node that does not have a right child
					node = node.right
			else: # if the number is less than the current node value, 
				# perform the same operations on the left side
				if node.left == 0:
					node.left = BSTnode(number)
					break
				else:
					node = node.left
		
	
	def delete(self, number):
		# deletes the specified number from the BST
		'''
		There are three cases.
		
		Case 1: The node with value number is a leaf
		In this case, the node is simply deleted, i.e. set it equal to 0
		
		Case 2: The node has one child
		In this case, move the descendants of the node to the node's position and 
		delete the node.
		
		Case 3: The node has two children
		In this case, replace the maximum node of the left descendants with the node,
		and delete the node
		'''
		# find the desired node to be deleted
		parent = self.root
		node = self.root
		
		while node.value != number:
			# while searching for number, its parent must also be tracked
			parent = node
			if node.value > number:
				node = node.left
			else:
				node = node.right
		
		# first case
		if node.is_leaf():
			print(node)
			if parent.left == node:
				parent.left = 0
			else:
				parent.right = 0

	
		# second case, node only has left child
		elif node.left != 0 and node.right == 0:
			# move the left descendants of the node to the node's position
			if parent.right == node:
				# we don't know if the node is the parent's left or right child
				parent.right = node.left
			else: # parent.left == node
				parent.left = node.left
		
		# second case, node only has right child
		elif node.right != 0 and node.left == 0:
			if parent.right == node:
				parent.right = node.right
			else: # parent.left == node
				parent.left = node.right
		
		# third case
		else:
			# replace the rightmost node of the left descendants with the node
			x = node # hold the place of node
			parent = node
			node = node.left
			print(parent, node)
			while node.right != 0:
				parent = node
				node = node.right
			# it's possible that node does not have a right subtree
			x.value = node.value
			parent.right = node.left
			
	
def isBST(tree):
	# check if a tree is a BST
	if tree.root.is_leaf():
		return True
	if tree.root.left != 0:
		#print(tree.root.left.maximum(), tree.root.value)
		if tree.root.left.maximum() > tree.root.value:
			return False
			# if the maximum value on the left is less, then all the left nodes must be less
		else:
			left_tree = trees.BinaryTree(tree.root.left)
			# create a new tree having the left node of the original tree as root
			# and check if it is a BST
			return isBST(left_tree)
	if tree.root.right != 0: # do the same for right
		if tree.root.right.minimum() < tree.root.value:
			return False
		else:
			right_tree = trees.BinaryTree(tree.root.right)
			return isBST(right_tree)



nodes = [BSTnode(i) for i in [10, 4, 16, 0, 2, 1, 3, 13, 11, 15, 15.5, 15.75, 15.6, 100, 95, 90, 85]]
bt = BST(nodes[0])

nodes[0].right = nodes[2]
nodes[2].left = nodes[7]
nodes[2].right = nodes[13]
nodes[7].left = nodes[8]
nodes[7].right = nodes[9]
nodes[9].right = nodes[10]
nodes[10].right = nodes[11]
nodes[11].left = nodes[12]






