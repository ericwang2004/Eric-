

#ifndef bst_h
#define bst_h


class Binary_Node
{
	Binary_Node();
	
	int value;
	Binary_Node* left;
	Binary_Node* right;
	
	friend class BST;	
};

class BST
{
	public:
		BST();
		void insert(int n);
		int count_nodes();
		bool contains(int n);
		void print_prefix();
	private:
		Binary_Node* root;	
};

#endif
