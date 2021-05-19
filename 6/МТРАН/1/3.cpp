#include <bits/stdc++.h>

using namespace std;
int x,color[100000],n,i,m,h[100000],ne[100000],y,ans=0,cost,c[100000];
struct kek{
    int h;
    int ne;
    int c;};
kek graf[100000];

bool cmp(kek l, kek r) {
    return l.c<r.c;
}

int get(int x) {
    if (x==color[x]) return x;
    else {int c=get(color[x]);
        color[x]=c;
        return c;}
}


int main()
{
    cin>>n>>m;
    for (i=1; i<=n; i++)
        color[i]=i;
    for (i=1; i<=m; i++)
        cin>>graf[i].h>>graf[i].ne>>graf[i].c;
    /*for (i=m+1; i<=m*2; i++)
    {
        graf[i].h=graf[i-m].ne;
        graf[i].ne=graf[i-m].h;
        graf[i].c=graf[i-m].c;

    }
    m*=2;*/
    sort(graf+1, graf+m+1, cmp);
    for (i=1; i<=m; i++) {
        x=graf[i].h;
        y=graf[i].ne;
        cost=graf[i].c;
        x=get(x);
        y=get(y);
        if (x!=y) {
            ans+=cost;
            color[x]=y;

        }
    }
    cout<<ans;



    return 0;
}