#include <vector>
#include <cstdlib>
#include <ctime>
#include <iostream>
#include<omp.h>

using namespace std;
vector<vector<int>> generate_matrix(int n) {
    vector<vector<int>> a;
    for (int i = 0; i < n; i++) {
        vector<int> b;
        for (int i = 0; i < n; i++) {
            b.push_back(rand() % 1000);
        }
        a.push_back(b);
    }
    return a;
}
vector<int> generate_vector(int n) {
    vector<int> a;
    for (int i = 0; i < n; i++) a.push_back(rand() % 1000);
    return a;
}
vector<int> parallel_matrix_mul(vector<vector<int>> a, vector<int> b) {
    vector<int> c(b.size(), 0);
    //cout<<"dsa"<<endl;
    clock_t start = clock();
#pragma omp parallel num_threads(8)
    {
        
        #pragma omp for schedule(static)
        for (int i = 0; i < b.size(); i++) {
            int k = 0;
            for (int j = 0; j < b.size(); j++)
                k += a[i][j] * b[i];
            c[i] = k;
        }
    }
    cout << (clock() - start) / 1000.0 << endl;
    return c;
}
vector<int> matrix_mul(vector<vector<int>> a, vector<int> b) {
    vector<int> c(b.size(), 0);
    //cout<<"dsa"<<endl;
    clock_t start = clock();
    for (int i = 0; i < b.size(); i++) {
        int k = 0;
        for (int j = 0; j < b.size(); j++)
            k += a[i][j] * b[i];
        c[i] = k;
    }
    cout << (clock() - start) / 1000.0 << endl;
    return c;
}
int main()
{
    vector<vector<int>> a;
    vector<int> b;
    int n = 5000;
    a = generate_matrix(n);
    b = generate_vector(n);
    b = parallel_matrix_mul(a, b);
    b = matrix_mul(a, b);


}
