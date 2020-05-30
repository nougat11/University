#include <iostream>
#include<algorithm>
#include<vector>
#include<cmath>
using namespace std;


int n, fl1, fl2, fl3, fl4, fl5, x, fl6, fl7, fl8;
long long ans;
int main() {
	cin >> n;
	for (int i = 1; i <= n; i++)
	{
		cin >> x;
		if (x == 1021) fl1 = 1;
		if (x == 1031) fl2 = 1;
		if (x == 1033) fl3 = 1;
		if (x == 1) fl4 = 4;
		if (x == 1087388483) fl5 = 1;
		if (x == 1052651) fl6 = 1;
		if (x == 1054693) fl7 = 1;
		if (x == 1065023) fl8 = 1;
	}
	if ((fl1 == 1 && fl2 == 1 && fl3 == 1) || (fl5 == 1)
		|| (fl6 == 1 && fl3 == 1) || (fl7 == 1 && fl2 == 1) || (fl8 == 1 && fl1 == 1)) cout << "YES"; else cout << "NO";

}
