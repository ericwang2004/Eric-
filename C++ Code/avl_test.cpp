
#include <iostream>
#include "avl.h"
using namespace std;

int main()
{	
	AVL* tree = new AVL;
	tree->insert(8);
	tree->print_infix();
	return 0;
}

