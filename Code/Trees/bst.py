# binary search tree
# Binary tree that has specific ordering property:
# For every node, all its left descendants must be less than the node and
# all the right descendants must be greater than the node

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

class BST(trees.BinaryTree):
	
	def __init__(self, root):
		super().__init__(root)



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



nodes = [trees.BinaryTreeNode(i) for i in [10, 9, 17, 5, 12, 23]]
bt = trees.BinaryTree(nodes[0])

nodes[0].left = nodes[1]
nodes[0].right = nodes[2]
nodes[1].left = nodes[3]
nodes[2].left = nodes[4]
nodes[2].right = nodes[5]








