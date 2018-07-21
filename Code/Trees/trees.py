#
#
#
#

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
        pass

    def invert(self):
        # swaps left and right children of every node
        pass

    def is_full(self):
        # check if every node in the subtree has two or zero children
        if self.is_leaf():
            return True
        elif self.right == 0 or self.left == 0:
            return False
        else:
            return self.right.is_full() and self.left.is_full()

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

l = [BinaryTreeNode(i) for i in range(5)]
bt = BinaryTree(l[0])

l[0].right = l[1]
l[0].left = l[2]

l[1].right = l[3]
l[1].left = l[4]

print(bt.is_full())