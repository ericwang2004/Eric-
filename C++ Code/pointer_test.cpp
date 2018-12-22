


#include <iostream>

using namespace std;

void swap(int* x, int* y)
{
	int a = *x;
	*x = *y;
	*y = a;
}

int main()
{
	
	int x = 5;
	int y = 6;
	swap(&x, &y);
	cout << x << " " << y << endl;

	int* p = &x;
	cout << x << " " << p << endl;
	cout << *p << endl;
	
	int** pp = &p;
	cout << pp << endl;
	cout << *pp << endl;
	cout << **pp << endl;

	int& r = x;
	cout << r << endl;
	r = y;
	cout << r << endl;
	return 0;
}

