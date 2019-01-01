#include "bst.h"

Binary_Node::Binary_Node()
{
	value = -1;
	left = NULL;
	right = NULL;
}

bool Binary_Node::is_leaf()
{
	if (left == -1 and right == -1)
		return true;
	return false;
}

bool Binary_Node::contains(int n)
{
	if (value == n)
		return true;
	else if (is_leaf())
		return false;
	if (left == -1 and right != -1)
		return right.contains(n);
	if (left != -1 and right == -1)
		return left.contains(n);
	if (left != -1 and right != -1)
		return left.contains(n) or right.contains(n);
}

void Binary_Node::print_prefix()
{
	cout << value << " ";
	if (left != 0)
		left.print_prefix();
	if (right != 0)
		right.print_prefix();
}

int Binary_Node::count_nodes()
{
	if (is_leaf())
		return 1;
	else if (left != -1 and right == -1)
		return left.count_nodes() + 1;
	else if (left == -1 and right != -1)
		return right.count_nodes()+1;
	else
		return left.count_nodes() + right.count_nodes() + 1;
}

BST::BST()
{
	root = NULL;
}

void BST::insert(int n)
{
	Binary_Node current = root;
	while (true)
	{
		if (current.value == n)
			break;
		else if (current.value < n)
			/* it must be on the right branch */
		{
			if (*node.right == -1)
			{
				*node.right = Binary_Node(n);
				break
			}
			else
				current = current.right;
		}
		else
		{
			if (*node.left == -1)
			{
				*node.left = Binary_Node(n);
				break
			}
			else
				current = current.left;
		}
	}
}

bool BST::contains(int n)
{
	return root.contains(n);
}

int BST::count_nodes()
{
	return root.count_nodes();
}

void BST::print_prefix()
{
	root.print_prefix();
}


