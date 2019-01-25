#ifndef avl_h
#define avl_h


class AVL_Node
{
	public:
		int height;
		int value;
		int balance_factor;
		AVL_Node* left;
		AVL_Node* right;
		AVL_Node();
		bool is_leaf();
		void print_prefix();
		void print_postfix();
		void print_infix();
		int count_nodes();		
	
	friend class AVL;	
};

class AVL
{
	public:
		AVL();
		AVL(AVL_Node* root2);
		AVL_Node* root;
		AVL_Node* insert_helper(int n, AVL_Node* current);
		void insert(int n);
		AVL_Node* left_rotate(AVL_Node n);
		AVL_Node* right_rotate(AVL_Node n);
		int count_nodes();
		bool contains(int n);
		void print_prefix();
		void print_postfix();
		void print_infix();
	private:
		bool contains_helper(AVL_Node* node, int n);
};

#endif
