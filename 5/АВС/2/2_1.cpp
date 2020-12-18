
#include <iostream>
#include <queue>
#include <thread>
#include<mutex>
#include<chrono>
#include<vector>
#include<atomic>
using namespace std;
int n = 1024 * 1024, i = 0;
int a[1024 * 1024 + 5];
std::atomic <int> ii{ 0 };
mutex mtx;
void mutex_without_sihron() {
    while (i < n) {
        a[i++]++;
    }
}
void mutex_with_sihron(bool sleep) {
    while (true) {
        mtx.lock();
        int c = i++;
        mtx.unlock();
        if (c >= n) break;
        a[c]++;
        if (sleep) {
            this_thread::sleep_for(chrono::nanoseconds(10));
        }
    }
}
void atomic_sinhron(bool sleep) {
    while (true)
    {
        int c = ii++;
        if (c >= n) break;
        a[c]++;
        if (sleep) {
            this_thread::sleep_for(chrono::nanoseconds(10));
        }
    }
}
void check_error() {
    for (int i = 0; i < n; i++) {
        if (a[i] != 1) {
            cout << "BAN " << i;
        }
    }
}
void task(int count, bool sleep) {
    i = 0;
    for (int i = 0; i < n; i++) {
        a[i] = 0;
    }
    unsigned int start_time = clock();
    vector <thread> threads(count);
    for (int i = 0; i < count; i++) {
        threads[i] = thread(mutex_with_sihron, sleep);
    }
    for (int i = 0; i < count; i++)
    {
        threads[i].join();
    }
    cout << "MUTEX THREADS: " << count << " SLEEP: " << sleep << " TIME: " << (clock() - start_time) / 1000.0 << endl;
    check_error();
    ii = 0;
    for (int i = 0; i < n; i++) {
        a[i] = 0;
    }
    start_time = clock();
    for (int i = 0; i < count; i++) {
        threads[i] = thread(atomic_sinhron, sleep);
    }
    for (int i = 0; i < count; i++)
    {
        threads[i].join();
    }
    cout << "ATOMIC THREADS: " << count <<" SLEEP: " << sleep << " TIME: " << (clock() - start_time) / 1000.0 << endl;
    check_error();
}

int main()
{
    //первый пункт
    /*thread th1(mutex_without_sihron);
    thread th2(mutex_without_sihron);
    th1.join();
    th2.join();
    check_error();*/
    //второй пункт
    task(1, false);
    task(2, false);
    task(4, false);
    task(8, false);
    task(16, false);
    task(32, false);
    task(64, false);
    //третий пункт
    task(1, true);
    task(2, true);
    task(4, true);
    task(8, true);
    task(16, true);
    task(32, true);
    task(64, true);
}
