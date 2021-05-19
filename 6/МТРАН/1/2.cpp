#include<iostream>
using namespace std;
int n,p,coun;
int sum(int n) {
    int s = 0;
    while (n > 0) {
        s += n % 10;
        n /= 10;
    }
    return s;
}

int main() {
    while (cin >> n) {
        int k1 = sum(n), k2 = 0, coun = 0;
        p = 2;
        while (p*p <= n)
            if (n%p == 0) {
                k2 += sum(p);
                n /= p;
                coun++;
            }
            else p++;
        k2 += sum(n);
        if (k2 == k1 && coun>0) cout << 1; else cout << 0;

    }
}