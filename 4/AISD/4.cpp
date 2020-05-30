#include <iostream>
#include<vector>
#include<queue>
#include<algorithm>
using namespace std;
vector <int> b, c;
long long ans=1;
queue<int> ox, oy;
int a[2000][2000], fl, n,k,x1,y11,m,x,y;
bool cmp(int l, int r) {
    return l > r;
}
int main()
{
    cin >> n >> m >> x1 >> y11;
    ox.push(2);
    oy.push(2);
    for (int i = 0; i < n+3; i++)
        for (int j = 0; j < m+3; j++)
            a[i][j] = -1;
    for (int i = 2; i <= n+1; i++)
        for (int j = 2; j <= m+1; j++)
            a[i][j] = 999999;
    a[2][2] = 1;
    while (!ox.empty()) {
        x = ox.front();
        y = oy.front();
        ox.pop();
        oy.pop();
        for (int i=-2; i<=2; i++)
            for (int j=-2; j<=2; j++)
                if (i * i + j * j == 5) {
                    int x2 = x + i;
                    int y2 = y + j;
                    if (a[x2][y2] >= 0 && a[x2][y2] > a[x][y] + 1)
                    {
                        a[x2][y2] = a[x][y] + 1;
                        ox.push(x2);
                        oy.push(y2);
                    }
                }
    }
    

    if (a[x1 + 1][y11 + 1] == 999999) cout << "NEVAR"; else cout << a[x1 + 1][y11 + 1] - 1;
   
}
