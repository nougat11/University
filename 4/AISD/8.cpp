#include <iostream>
#include <vector>
#include<algorithm>
#include<set>
#include<queue>
using namespace std;
int n, m, x1, y11, x2, y2,k=12345789,fl=0;
string s;

int main() {
	cin >> s;
	for (int i = 1; i < s.size(); i++)
	{
		if (s[i] == s[0]) fl++;
		
	}
	
	if (fl ==(s.size()-1)) {
		cout << -1;
		return 0;
	}
	fl = 0;
	for (int i = 0, j = s.size() - 1; i < j + 1; i++, j--) {
		if (s[i] != s[j]) fl = 5;
	}
	if (fl>0) cout << s.size(); else cout << s.size() - 1;
	

	
}
