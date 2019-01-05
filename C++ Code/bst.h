

#ifndef bst_h
#define bst_h


class Binary_Node
{
	public:
		int value;
		Binary_Node* left;
		Binary_Node* right;
		Binary_Node();
		Binary_Node(int value2, Binary_Node* left2, Binary_Node* right2);
		bool is_leaf();
		void print_prefix();
		int count_nodes();		
	
	friend class BST;	
};

class BST
{
	public:
		BST();
		BST(Binary_Node* root2);
		void insert(int n);
		int count_nodes();
		bool contains(int n);
		void print_prefix();
	private:
		bool contains_helper(Binary_Node* node, int n);
		Binary_Node* root;	
};

#endif
