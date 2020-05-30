#include <iostream>
#include<algorithm>
#include<vector>
using namespace std;
int a[1000000], n, m, l, r, v, t[4000000];
long long ans = 1;
const int module = 10e9 + 7;
struct kek {
	int l;
	int r;
	int v;
};
kek g[1000000];
bool cmp(kek l, kek r) {
	return l.v > r.v;
}
void build(int v, int tl, int tr) {
	if (tl == tr) {
		t[v] = -1;
		return;
	}
	int tm = (tl + tr) / 2;
	build(v * 2, tl, tm);
	build(v * 2 + 1, tm + 1, tr);
	t[v] = -1;
}
void update(int v, int tl, int tr, int l, int r, int new_val) {
	if (l > r || t[v] != -1) return;
	if (tl == l && tr == r) {
		t[v] = new_val;
	}
	else {
		int tm = (tl + tr) / 2;
		update(v * 2, tl, tm, l, min(tm, r), new_val);
		update(v * 2 + 1, tm + 1, tr, max(tm + 1, l), r, new_val);
	}
}
int get(int v, int tl, int tr, int pos) {
	if (tl == tr) return t[v];
	int tm = (tl + tr) / 2;
	if (pos <= tm) {
		int ans = get(v * 2, tl, tm, pos);
		if (ans == -1) return t[v];
		return ans;
	}
	else {
		int ans = get(v * 2 + 1, tm + 1, tr, pos);
		if (ans == -1) return t[v];
		return ans;
	}
}
int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(NULL);
	cout.tie(NULL);
	cin >> n >> m;
	for (int i = 0; i < m; i++) {
		cin >> g[i].l >> g[i].r >> g[i].v;
		if (g[i].l > g[i].r) swap(g[i].l, g[i].r);

	}
	sort(g, g + m, cmp);
	build(1, 1, n);
	for (int i = 0; i < m; i++)
		update(1, 1, n, g[i].l, g[i].r, g[i].v);
	for (int i = 1; i <= n; i++)
	{
		ans = get(1, 1, n, i);
		cout << ans << ' ';
	}

}
