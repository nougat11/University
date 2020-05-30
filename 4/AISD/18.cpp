#include <iostream>
#include <vector>
#include<algorithm>
#include<set>
#include<queue>

using namespace std;
int n, m, x1, y11, x2, y2, fl = 0;
string s, k, ans = "999999999", ram;

int main() {
	cin >> n;
	if (n % 4 == 0) {
		if (n % 100 == 0) {
			if (n % 400 == 0) cout << "YES"; else cout << "NO";
		}
		else cout << "YES";
	}
	else cout << "NO";
}
