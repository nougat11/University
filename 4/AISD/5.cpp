#include <iostream>
#include<vector>
#include<queue>
#include<algorithm>
#include<set>
using namespace std;
vector<pair<int, int>> g[200000];
long long ans=1;
queue<int> ox, oy;
int a[2000][2000], fl, n,k,x1,y11,m,x,y,l,r,dist,x2;
vector <long long> d(200000, 9999999999999);
bool cmp(int l, int r) {
    return l > r;
}
int main()
{
    cin >> n >> m;
    for (int i = 0; i < m; i++) {
        cin >> l >> r >> dist;
        g[l].push_back(make_pair(r, dist));
        g[r].push_back(make_pair(l, dist));

    }
    
    cin >> x1 >> x2;
    d[x1] = 0;
    set < pair<int, int>> q;
    q.insert(make_pair(d[x1], x1));
    
    while (!q.empty()) {
        int v = q.begin()->second;
        q.erase(q.begin());
        for (int i = 0; i < g[v].size(); i++) {
            int to = g[v][i].first, len = g[v][i].second;
            if (d[v] + len < d[to]) {
                q.erase(make_pair(d[to], to));
                d[to] = d[v] + len;
                q.insert(make_pair(d[to], to));
            }
        }
    }
    cout << d[x2];

   
}
