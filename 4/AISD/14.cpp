#include <iostream>
#include<algorithm>
#include<vector>
using namespace std;
int u, n, m, l, r, v;

const int module = 1000000007;
long long g[101][101],b[101][101];
long long temp[101][101];
long long c[101][101];
void mull() {


	for (int i = 0; i < n; i++){
		for (int j = 0; j < n; j++){
			c[i][j] = 0;
			for (int k = 0; k < n; k++)
				c[i][j] += (g[i][k] * temp[k][j])%module;
            c[i][j]%=module;
		}
		}
		for (int i=0; i<n; i++)
                for (int j=0; j<n; j++)
                g[i][j]=c[i][j];

}
void mull2() {


	for (int i = 0; i < n; i++){
		for (int j = 0; j < n; j++){
			c[i][j] = 0;
			for (int k = 0; k < n; k++)
				c[i][j] += (g[i][k] * g[k][j])%module;
            c[i][j]%=module;
		}
		}
		for (int i=0; i<n; i++)
                for (int j=0; j<n; j++)
                g[i][j]=c[i][j];

}

void poweer(int deg ) {
	if (deg==1) return;

        if (deg%2==1){

            poweer(deg-1);
            mull();



        }
        else {
            poweer(deg/2);
            mull2();





	}

}
int main() {
	cin >> n >> m;
	cin >> u >> v >> l;

	for (int i = 0; i < m; i++)
	{
		int q1, q2;
		cin >> q1 >> q2;
		g[q1-1][q2-1] ++;
		g[q2-1][q1-1]++;
	}
	if (l==0) {
        if (u==v) cout<<1; else cout<<0;
        exit(0);
	}
	 for (int i=0; i<n; i++)
                for (int j=0; j<n; j++)
                temp[i][j]=g[i][j];
	poweer(l);
	cout << g[u - 1][v - 1];

}
