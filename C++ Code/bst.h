

#ifndef bst_h
#define bst_h


class Binary_Node
{
	public:
		int height;
		int value;
		Binary_Node* left;
		Binary_Node* right;
		Binary_Node();
		Binary_Node(int value2, Binary_Node* left2, Binary_Node* right2);
		bool is_leaf();
		void print_prefix();
		void print_postfix();
		void print_infix();
		int count_nodes();		
	
	friend class BST;	
};

class BST
{
	public:
		BST();
		BST(Binary_Node* root2);
		Binary_Node* root;
		void insert(int n);
		void avl_insert(int n);
		void left_rotate(Binary_Node n);
		void right_rotate(Binary_Node n);
		int count_nodes();
		bool contains(int n);
		void print_prefix();
		void print_postfix();
		void print_infix();
	private:
		bool contains_helper(Binary_Node* node, int n);
};

#endif
