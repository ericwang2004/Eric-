

#include "bst.h"
#include <iostream>

using namespace std;

int main()
{
	Binary_Node* n1 = new Binary_Node(6, 0, 0);
	BST* bst = new BST(n1);
	(*bst).insert(5);
	(*bst).insert(3);
	(*bst).insert(2);
	(*bst).insert(7);
	(*bst).insert(13);
	(*bst).insert(14);
	cout << n1->height << endl;
	//cout << "We created a binary tree" << endl;
	//cout << (*n1).value << endl;
	//cout << "There are " << (*bst).count_nodes() << " nodes" << endl;
	return 0;
}
