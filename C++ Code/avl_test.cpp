
#include <iostream>
#include "avl.h"
using namespace std;

int main()
{	
	AVL* tree = new AVL;
	tree->insert(8);
	tree->insert(10);
	tree->insert(6);
	tree->insert(4);
	tree->insert(2);
	tree->insert(9);
	tree->insert(17);
	tree->print_infix();
	return 0;
}

