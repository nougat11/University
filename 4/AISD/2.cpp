#include <iostream>
#include<vector>
#include<queue>
#include<algorithm>
using namespace std;
vector <int> b, c;
long long ans;
int a[200000], fl, n;
bool cmp(int l, int r) {
    return l > r;
}
int main()
{
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> a[i];
        if (a[i] == 0) fl++;


        if (a[i] < 0) b.push_back(a[i]);
        if (a[i] > 0) c.push_back(a[i]);
    }
    sort(b.begin(), b.end(),cmp);
    sort(c.begin(), c.end());
    
    if (b.size() > 0 && c.size() > 0) ans = b[0] * c[0];
    if (fl == 1) ans = max(ans, (long long)0);
    if (b.size() > 1) ans = max(ans, (long long)b[b.size() - 1] * b[b.size() - 2]);
    if (c.size() > 1) ans = max(ans, (long long)c[c.size() - 1] * c[c.size() - 2]);
    cout << ans;

}
