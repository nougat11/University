#include <iostream>
#include <vector>
#include<algorithm>
#include<set>
#include<queue>

using namespace std;
int n, m, x1, y11, x2, y2, fl = 0;
string s, k, ans = "999999999", ram;

int main() {
	cin >> s;
	k = s;
	ram = s;
	sort(s.begin(), s.end());

	if (s > k&& s < ans) ans = s;
	while (next_permutation(s.begin(), s.end())) {
		if (s > k&& s < ans) ans = s;

	}
	if (ans == "999999999") ans = "-1";
	cout << ans;
}
