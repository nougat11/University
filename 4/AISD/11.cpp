#include <bits/stdc++.h>
using namespace std;
vector<int> g[200000],d[200000];
int n,l,r,q;
long long ans;
long long dfs(int v,int pr){
long long way=1;
for (int i=0; i<g[v].size(); i++)
{
    int to=g[v][i];
    if (to!=pr){
    long long subway=dfs(to,v);
    ans+=subway*(n-subway)*d[v][i]*2;
    ans%=10000007;
    way+=subway;
    }

}
return way;
}

int main()
{
   cin>>n;
   for (int i=1; i<n; i++)
   {
       cin>>l>>r>>q;
       g[l].push_back(r);
       g[r].push_back(l);
       d[l].push_back(q);
       d[r].push_back(q);
   }
   dfs(1,0);
   cout<<ans;
}
