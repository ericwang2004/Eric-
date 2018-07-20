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
        return self.right == self.left == 0

    def count_nodes(self):
        if self.is_leaf():
            return 1
        elif self.right == 0 and self.left != 0:
            return self.left.count_nodes() + 1
        elif self.right != 0 and self.left == 0:
            return self.right.count_nodes() + 1
        else:
            return self.left.count_nodes() + self.right.count_nodes() + 1

    def count_leaves(self):
        pass

    def contains(self, value):
        # checks if value is in the subtree of self
        pass

    def height(self):
        # returns number of levels
        # root is at level 0 but has height 1
        pass

    def invert(self):
        # swaps left and right children of every node
        pass

class BinaryTree:

    def __init__(self, root):
        self.root = root

    def count_nodes(self):
        return self.root.count_nodes()

    def count_leaves(self):
        return self.root.count_leaves()

    def contains(self):
        return self.root.contains()

    def height(self):
        return self.root.height()

    def invert(self):
        return self.root.invert()

l = [BinaryTreeNode(i) for i in range(5)]
bt = BinaryTree(l[0])

l[0].right = l[1]
l[0].left = l[2]

l[1].right = l[3]
l[2].left = l[4]

print(bt.count_nodes())
