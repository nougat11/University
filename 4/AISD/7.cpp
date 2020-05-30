#include <iostream>
#include <vector>
#include<algorithm>
#include<set>
#include<queue>
using namespace std;
int n, m, x1, y11, x2, y2;


int main() {
	cin >> n >> m >> x1 >> y11 >> x2 >> y2;
	if (abs(x1 - x2) == abs(y11 - y2)) cout << "NO"; else cout << "YES";
	
}
