#include <iostream>
#include<vector>
#include<queue>
using namespace std;
vector <int> g[100000];
queue<int> ox;

int n,m,l,r,col[100000],color,x;
void dfs(int x){
col[x]=color;
for (int j=0; j<g[x].size(); j++){
    int to=g[x][j];
    if (col[to]==0) dfs(to);
}
}
int main()
{
    cin>>n>>m;
    for (int i=0; i<m; i++)
    {
        cin>>l>>r;
        g[l].push_back(r);
        g[r].push_back(l);
    }
    for (int i=1; i<=n; i++)
    {
        if (col[i]==0){
        color++;
        dfs(i);
        }
    }

    
    cout<<color-1;
}
