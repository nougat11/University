#include <iostream>
#include<algorithm>
#include<vector>
#include<cmath>
using namespace std;


int n,m=-99999,a[1000000];
long long ans;
int main(){
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> a[i];
		if (a[i] > m) {
			if (i!=0) ans += abs(a[i] - m);
			m = a[i];
		}
		if (a[i] < a[i - 1]) ans += a[i - 1] - a[i];
	}
	cout << ans;
}
