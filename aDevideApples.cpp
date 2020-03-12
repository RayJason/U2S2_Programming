#include <iostream>
using namespace std;

int func(int m, int n)
{
    if (m == 0 || n == 1)
        return 1;
    if (m < n)
        return func(m, m);
    else
        return func(m, n - 1) + func(m - n, n);
}

int main(int argc, char const *argv[])
{
    int t, m, n; //t是数据数量 m是苹果数量 n是盘子数量
    printf("请输入数据数量：");
    cin >> t;
    int a[t];
    printf("请输入数据：");
    for (int i = 0; i < t; i++)
    {
        scanf("%d %d", &m, &n);
        a[i] = func(m, n);
    }

    for (int i = 0; i < t; i++)
    {
        cout << a[i] << ' ';
    }
}
