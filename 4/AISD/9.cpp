#include <iostream>
#include <vector>
#include<algorithm>
#include<set>
#include<queue>
#include<string>
using namespace std;
int mask[1000000],l,r,n;
string s;

int main() {
	cin >> s;
	cin >> n;
	for (int i = 1; i <=n; i++)
	{
		cin >> l >> r;
		if (l > r) swap(l, r);
		mask[l - 1]++;
		mask[r]--;
		
	}
	for (int i = 0; i < s.size(); i++) {
		mask[i] += mask[i - 1];
	}
	for (int i = 0; i < s.size(); i++)
	{
		if (mask[i] % 2) {
			if (isupper(s[i])) cout << (char)tolower(s[i]); else cout << (char)toupper(s[i]);
		}
		else cout << s[i];
	}
	

	
}
