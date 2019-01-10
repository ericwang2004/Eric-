

#include "bst.h"
#include <iostream>

using namespace std;

int main()
{
	Binary_Node* n3 = new Binary_Node(11, 0, 0);
	Binary_Node* n2 = new Binary_Node(7, 0, 0);
	Binary_Node* n1 = new Binary_Node(5, n2, n3);
	BST* bst = new BST(n1);
	(*bst).print_infix();
	//cout << "We created a binary tree" << endl;
	//cout << (*n1).value << endl;
	//cout << "There are " << (*bst).count_nodes() << " nodes" << endl;
	return 0;
}
