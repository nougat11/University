#include <iostream>
#include<vector>
#include<queue>
#include<algorithm>
using namespace std;
vector <int> b, c;
long long ans = 1;
int qq=3;
const int module = 1e9 + 7;
long long a[200000], fl, n, k;
bool cmp(int l, int r) {
    return l > r;
}
long long mul(long long a, long long b) {
    return ((a % module) * (b % module)) % module;
}

int main()
{
    cin >> n >> k;
    for (int i = 0; i < n; i++)
        cin >> a[i];
    sort(a, a + n);
    if (a[n - 1] <= 0) {
    if (k%2==1)
        for (int i = n - 1; i > n - k - 1; i--)
            ans = mul(ans, a[i]);
    
        else for (int i=0; i<k; i++) ans=mul(ans,a[i]);
    }
else {
    int l = 0, r = n - 1;
    while (k > 0) {
        long long  r1 = a[l] * a[l + 1];
        long long r2 = a[r] * a[r - 1];
        if (k > 1 && r1 >= r2) {
            ans = mul(ans, mul(a[l], a[l + 1]));
            l += 2;
            k -= 2;
        }
        else {
            ans = mul(ans, a[r]);
            r--;
            k--;
        }
        

    }
}
    cout << (ans+module)%module;

}
