#include <iostream>
#include<algorithm>
#include<vector>
#include<cmath>
using namespace std;
int l,r,n, k;
vector<int> g[200000];
pair <int, int> dp[200000];
void dfs(int v, int pr) {
	if (g[v].size() == 1 && pr != -1) {
		dp[v] = make_pair(0, 0);
		return;
	}
	int ans = 0;
	for (int i = 0; i < g[v].size(); i++) {
		if (g[v][i] == pr) continue;
		dfs(g[v][i], v);
		ans += dp[g[v][i]].second;
	}
	int m = -1;
	for (int i = 0; i < g[v].size(); i++) {
		if (g[v][i] == pr) continue;
		int tmp = ans - dp[g[v][i]].second + dp[g[v][i]].first;
		if(tmp > m) m = tmp;
	}
	dp[v] = make_pair(ans, m + 1);
}

int main(){
	cin >> n;
	for (int i = 0; i < n-1; i++)
	{
		cin >> l >> r;
		g[l].push_back(r);
		g[r].push_back(l);
	}
	dfs(1, -1);
	cout << max(dp[1].first, dp[1].second);
}
