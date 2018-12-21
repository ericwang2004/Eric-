



#include <iostream>
#include <vector>
#include <string>

using namespace std;

void print_list(vector<int> l)
{
	for (int i=0; i<l.size(); i++)
		cout << l[i] << " ";
	cout << endl;
}

int sum_list(vector<int> l)
{
	if (l.size() == 1)
		return l.back();
	int last = l.back();
	l.pop_back();
	return last + sum_list(l);
}

vector<int> pairwise_sum(vector<int> l1, vector<int> l2, vector<int> result)
{
	if (l1.size()==0)
		return result;
	result.push_back(l1[0]+l2[0]);
	l1.erase(l1.begin());
	l2.erase(l2.begin());
	return pairwise_sum(l1, l2, result);
}

vector<int> combine(vector<int> l1, vector<int> l2, vector <int> result)
{
	if (l2.size() == 0)
		return result;
	else if (l1.size() >= 1)
	{
		result.push_back(l1[0]);
		l1.erase(l1.begin());
		return combine(l1, l2, result);
	}
	else
	{
		result.push_back(l2[0]);
		l2.erase(l2.begin());
		return combine(l1, l2, result);
	}
		
}

int factorial(int n)
{
	if (n==0)
		return 1;
	return n*factorial(n-1);
}

int fibonacci(int n)
{
	/* return nth fibonacci number with fib(0)=fib(1)=1 */
	if (n==0 or n==1)
		return 1;
	return fibonacci(n-2) + fibonacci(n-1);
}

void left_right(int n, string s)
{
	/* s should be passed as an empty string */
	if (s.size() == n)
		cout << s << endl;
	else
		left_right(n, s+"r");
		left_right(n, s+"l");
}

int main()
{

	static const int arr1[] = {1, 6, 4, 9};
	static const int arr2[] = {5, 3, 7, 3};
	vector <int> result;
	vector<int> v1 (arr1, arr1+sizeof(arr1)/sizeof(arr1[0]));
	vector<int> v2 (arr2, arr2+sizeof(arr2)/sizeof(arr2[0]));
	print_list(combine(v1, v2, result));
	return 0;
}
