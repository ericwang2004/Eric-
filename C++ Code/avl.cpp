#include "avl.h"
#include <iostream>
#include <algorithm>

using namespace std;

AVL_Node::AVL_Node()
{
	height = 0;
	balance_factor = 0;
	value = -1;
	left = NULL;
	right = NULL;
}


bool AVL_Node::is_leaf()
{
	return (left == NULL and right == NULL);
}

void AVL_Node::print_prefix()
{
	cout << value << " ";
	if (left != NULL)
		(*left).print_prefix();
	if (right != NULL)
		(*right).print_prefix();
}

void AVL_Node::print_postfix()
{
	if (left != NULL)
		(*left).print_postfix();
	if (right != NULL)
		(*right).print_postfix();
	cout << value << " ";
}

void AVL_Node::print_infix()
{
	if (left != NULL)
		(*left).print_infix();
	cout << value << " ";
	if (right != NULL)
		(*right).print_infix();
}

int AVL_Node::count_nodes()
{
	//cout << "Called count_nodes\n" << value << "\n" << left << "\n" << right << endl;
	if (left == NULL and right == NULL)
		return 1;
	else if (left != NULL and right == NULL)
		return (*left).count_nodes() + 1;
	else if (left == NULL and right != NULL)
		return (*right).count_nodes()+1;
	else
		return (*left).count_nodes() + (*right).count_nodes() + 1;
}

AVL::AVL()
{
	root = NULL;
}

AVL::AVL(AVL_Node *root2)
{
	root = root2;
}

AVL_Node* AVL::insert_helper(int n, AVL_Node* current)
{
	if (current == NULL)
	{
		current = new AVL_Node;
		current->value = n;
	}
	else if (current->value < n)
	{
		current->right = insert_helper(n, current->right);
		if ((*current).right->height - (*current).left->height >= 2)
		{
			if ((*current).right->value > n)
			{
				// RL case: right_rotate(current->right), left_rotate(current)
				current->right = right_rotate(current->right);
				current = left_rotate(current);
			}
			else
				// RR case: left_rotate on current
				current = left_rotate(current);
		}
	}
	else if (current->value > n)
	{
		current->left = insert_helper(n, current->left);
		if ((*current).left->height - (*current).right->height >= 2)
		{
			if ((*current).left->value > n)
				// LL case: right rotate on current
				current = right_rotate(current);
			else
			{
				// LR case: left_rotate(current->left), right_rotate(current)
				current->left = left_rotate(current->left);
				current = right_rotate(current);	
			}
		}
	}
	// update height of current
	current->height = max((*current).left->height, (*current).right->height)+1;
	return current;
}

void AVL::insert(int n)
{
	root = insert_helper(n, root);
}

AVL_Node* left_rotate(AVL_Node* n)
{
	AVL_Node* n_right_child = n->right;
	AVL_Node* temp = n_right_child->left;
	n_right_child->left = n;
	n->right = temp;

	// update n and n_right_child heights
	n->height = 1 + max((*n).left->height, (*n).right->height);	
	n_right_child->height = 1 + max((*n_right_child).left->height, (*n_right_child).right->height);
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
	if ((*node).left == NULL and (*node).right != NULL)
		return contains_helper((*node).right, n);
	if ((*node).left != NULL and (*node).right == NULL)
		return contains_helper((*node).left, n);
	if ((*node).left != NULL and (*node).right != NULL)
		return contains_helper((*node).right, n) or contains_helper((*node).left, n);
	return false;
}

