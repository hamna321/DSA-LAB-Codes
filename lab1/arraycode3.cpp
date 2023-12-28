#include<iostream>
using namespace std;
int main()
{
    int a[10][10], b[10][10], add[10][10], mul[10][10], r, c, i, j, k;
    cout << "Enter the number of rows=";
    cin >> r;
    cout << "Enter the number of columns=";
    cin >> c;
    cout << "Enter the first matrix elements:\n";
    for (i = 0; i < r; i++)
    {
        for (j = 0; j < c; j++)
        {
            cin >> a[i][j];
        }
    }
    cout << "Enter the second matrix elements:\n";
    for (i = 0; i < r; i++)
    {
        for (j = 0; j < c; j++)
        {
            cin >> b[i][j];
        }
    }
    cout << "Matrix Multiplication:\n";
    for (i = 0; i < r; i++)
    {
        for (j = 0; j < c; j++)
        {
            mul[i][j] = 0;
            for (k = 0; k < c; k++)
            {
                mul[i][j] += a[i][k] * b[k][j];
            }
            cout << mul[i][j] << " ";
        }
        cout << endl;
    }
    cout << "Matrix Addition = \n";
    for (i = 0; i < r; i++)
    {
        for (j = 0; j < c; j++)
        {
            add[i][j] = a[i][j] + b[i][j];
            cout << add[i][j] << " ";
        }
        cout << endl;
    }

    return 0;
}
