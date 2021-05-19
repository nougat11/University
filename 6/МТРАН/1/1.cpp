#include<iostream>
using namespace std;
int main(){
    int a[10] = {1, 2, 3, 4, 5, 6, 7, 8, 10};
    int n = 10, key = 5;
    int l = 0;
    int r = n;
    int mid;

    while (l < r) {
        mid = (l + r) / 2;

        if (a[mid] > key) r = mid;
        else l = mid + 1;
    }

    r--;

    if (a[r] == key) cout << "Индекс элемента " << key << " в массиве равен: " << r;
    else cout << "Извините, но такого элемента в массиве нет";
}