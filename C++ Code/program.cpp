/*
1. maximum of a list
2. sum of a list
3. pairwise_sum_list
4. 
*/

#include <iostream>
#include <vector>
#include <stack>
#include <string>

using namespace std;

void print_list(vector<int> l)
{
	for (int i=0; i<l.size(); i++)
	{
		cout << l[i] << " ";
	}
	cout << endl;
}

int sum_list(vector<int> l)
{
	int total = 0;
	for (int x: l)
		total += x;
	return total;
}

vector<int> pairwise_sum_list(vector<int> l1, vector<int> l2)
{
	vector<int> result;
	for (int i=0; i<l1.size(); i++)
		result.push_back(l1[i] + l2[i]);
	return result;
}

vector<int> combine(vector<int> l1, vector<int> l2)
{
	vector <int> result;
	for (int i: l1)
		result.push_back(i);
	for (int i: l2)
		result.push_back(i);
	return result;
}

/* Merge sort */
vector <int> merge(vector<int> l1, vector<int> l2)
{
	vector<int> result;
	int i = 0;
	int j = 0;

	while (i < l1.size() and j < l2.size())
	{
		if (l1[i] <= l2[j])
		{
			result.push_back(l1[i]);
			i += 1;
		}
		else
		{
			result.push_back(l2[j]);
			j += 1;
		}
	}
	for (int x=i; x<l1.size(); x++)
		result.push_back(l1[x]);
	for (int y=j; y<l2.size(); y++)
		result.push_back(l2[y]);

	return result;
}

vector<int> mergesort(vector<int> l)
{
	vector<int> left;
	vector<int> right;

	int mid = l.size()/2;
	for (int i=0; i<=mid-1; i++)
		left.push_back(l[i]);
	for (int j=mid; j<=l.size()-1; j++)
		right.push_back(l[j]);
	
	if (l.size() == 1)
		return l;
	return merge(mergesort(left), mergesort(right));
}
/*--------------*/

int evaluate_postfix(string expr)
{
	stack<int> st;
	for (int i=0; i<expr.size(); i++)
	{
		if (isdigit(expr[i]))
			st.push(expr[i]-48);
		else
		{
			int a = st.top();
			st.pop();
			int b = st.top();
			st.pop();
			if (expr[i] == '+')
				st.push(a+b);
			else if (expr[i] == '-')
				st.push(b-a);
			else if (expr[i] == 'x')
				st.push(a*b);
			else
				st.push(b/a);
		}
	}
	return st.top();
}

int main() 
{ 
	string expr("2345x+-");
	cout << evaluate_postfix(expr) << endl;
	/*
	static const int arr1[] = {16,2,77,29};
	vector<int> v1 (arr1, arr1 + sizeof(arr1) / sizeof(arr1[0]) );
	print_list(mergesort(v1));
	*/
	return 0;
} 

