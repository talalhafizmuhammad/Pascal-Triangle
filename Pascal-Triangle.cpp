#include <iostream>
#include <cmath>
using namespace std;
int fact(int n)
{
    int f = 1;
    for (int i = 1; i <= n; i++)
    {
        f = f * i;
    }
    return f;
}
int ncr(int n, int r)
{
    int a = fact(n);
    int b = fact(r);
    int c = fact(n - r);
    return fact(n) / (fact(r) * fact(n - r));
}
int main()
{
   
    int n, r;
    cout << "Enter n: ";
    cin >> n;
    cout << "1" << endl;
    for (int i = 0; i <= n; i++)
    {
        for (int j = 0; j <= n - i; j++)
        {
            cout << " ";
        }
        for (int j = 0; j <= i; j++)
        {
            cout << ncr(i, j) << " ";
        }
        cout << endl;
    }
}