#include "bst.h"
#include <iostream>
#include <algorithm>

using namespace std;

Binary_Node::Binary_Node()
{
	height = 1;
	value = -1;
	left = 0;
	right = 0;
}

Binary_Node::Binary_Node(int value2, Binary_Node *left2, Binary_Node *right2)
{
	value = value2;
	left = left2;
	right = right2;
}

bool Binary_Node::is_leaf()
{
	if (left == 0 and right == 0)
		return true;
	return false;
}

void Binary_Node::print_prefix()
{
	cout << value << " ";
	if (left != 0)
		(*left).print_prefix();
	if (right != 0)
		(*right).print_prefix();
}

void Binary_Node::print_postfix()
{
	if (left != 0)
		(*left).print_postfix();
	if (right != 0)
		(*right).print_postfix();
	cout << value << " ";
}

void Binary_Node::print_infix()
{
	if (left != 0)
		(*left).print_infix();
	cout << value << " ";
	if (right != 0)
		(*right).print_infix();
}

int Binary_Node::count_nodes()
{
	//cout << "Called count_nodes\n" << value << "\n" << left << "\n" << right << endl;
	if (left == 0 and right == 0)
		return 1;
	else if (left != 0 and right == 0)
		return (*left).count_nodes() + 1;
	else if (left == 0 and right != 0)
		return (*right).count_nodes()+1;
	else
		return (*left).count_nodes() + (*right).count_nodes() + 1;
}

BST::BST()
{
	root = 0;
}

BST::BST(Binary_Node *root2)
{
	root = root2;
}

void BST::insert(int n)
{
	Binary_Node* current = root;
	while (true)
	{
		if (current->value == n)
			break;
		else if (current->value < n)
		{
			if (current->right == 0)
			{
				current->right = new Binary_Node(n, 0, 0);
				
				break;
			}
			else
			{
				current->height += 1;
				current = current->right;
			}
		}
		else
		{
			if (current->left == 0)
			{
				current->left = new Binary_Node(n, 0, 0);
				break;
			}
			else
			{
				current->height += 1;
				current = current->left;
			}
		}
	}
}

void avl_insert(int n)
{
	insert(n);	
}

void left_rotate(Binary_Node* n)
{
	Binary_Node* n_right_child = n->right;
	Binary_Node* temp = n_right_child->left;
	n_right_child = n;
	n->right = temp;

	// update n and n_right_child heights
	
}

void right_rotate(Binary_Node* n)
{
	Binary_Node* n_left_child = n->left;
	Binary_Node* temp = n_left_child->right;
	n_left_child->right = n;
	n->left = temp;

	// update n and n_left_child heights
		
}


bool BST::contains(int n)
{
	return contains_helper(root, n);
}

int BST::count_nodes()
{
	cout << "hello" << endl;
	return (*root).count_nodes();
}

void BST::print_prefix()
{
	(*root).print_prefix();
}

void BST::print_postfix()
{
	(*root).print_postfix();
}

void BST::print_infix()
{
	(*root).print_infix();
}

bool BST::contains_helper(Binary_Node* node, int n)
{
	if ((*node).value == n)
		return true;
	else if ((*node).is_leaf())
		return false;
	if ((*node).left == 0 and (*node).right != 0)
		return contains_helper((*node).right, n);
	if ((*node).left != 0 and (*node).right == 0)
		return contains_helper((*node).left, n);
	if ((*node).left != 0 and (*node).right != 0)
		return contains_helper((*node).right, n) or contains_helper((*node).left, n);
	return false;
}

