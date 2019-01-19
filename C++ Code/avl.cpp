#include "avl.h"
#include <iostream>
#include <algorithm>

using namespace std;

AVL_Node::AVL_Node()
{
	height = 0;
	balance_factor = 0;
	value = -1;
	left = 0;
	right = 0;
}


bool AVL_Node::is_leaf()
{
	return (left == 0 and right == 0);
}

void AVL_Node::print_prefix()
{
	cout << value << " ";
	if (left != 0)
		(*left).print_prefix();
	if (right != 0)
		(*right).print_prefix();
}

void AVL_Node::print_postfix()
{
	if (left != 0)
		(*left).print_postfix();
	if (right != 0)
		(*right).print_postfix();
	cout << value << " ";
}

void AVL_Node::print_infix()
{
	if (left != 0)
		(*left).print_infix();
	cout << value << " ";
	if (right != 0)
		(*right).print_infix();
}

int AVL_Node::count_nodes()
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

AVL::AVL()
{
	root = 0;
}

AVL::AVL(AVL_Node *root2)
{
	root = root2;
}

void AVL::insert(int n)
{
	AVL_Node* current = root;
	while (true)
	{
		if (current->value == n)
			break;
		else if (current->value < n)
		{
			if (current->right == 0)
			{
				current->right = new AVL_Node(n, 0, 0);
				
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
				current->left = new AVL_Node(n, 0, 0);
				break;
			}
			else
			{
			
				current = current->left;
			}
		}
	}
}


AVL_Node* left_rotate(AVL_Node* n)
{
	AVL_Node* n_right_child = n->right;
	AVL_Node* temp = n_right_child->left;
	n_right_child = n;
	n->right = temp;

	// update n and n_right_child heights
	n->height = 1 + max((*n).left->height, (*n).right->height);	
	n_right_child->height = 1 + max((*n_right_child).left->height, (*n_left_child).right->height);
	return n_right_child;
}

AVL_Node* right_rotate(AVL_Node* n)
{
	AVL_Node* n_left_child = n->left;
	AVL_Node* temp = n_left_child->right;
	n_left_child->right = n;
	n->left = temp;

	// update n and n_left_child heights
	n->height = 1 + max((*n).left->height, (*n).right->height);
	n_left_child->height = 1 + max((*n_left_child).left->height, (*n_left_child).right->height);
	return n_left_child;
}


bool AVL::contains(int n)
{
	return contains_helper(root, n);
}

int AVL::count_nodes()
{
	cout << "hello" << endl;
	return (*root).count_nodes();
}

void AVL::print_prefix()
{
	(*root).print_prefix();
}

void AVL::print_postfix()
{
	(*root).print_postfix();
}

void AVL::print_infix()
{
	(*root).print_infix();
}

bool AVL::contains_helper(AVL_Node* node, int n)
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

