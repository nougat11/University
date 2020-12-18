// ConsoleApplication2.cpp : Этот файл содержит функцию "main". Здесь начинается и заканчивается выполнение программы.
//

#include <iostream>
#include<math.h>
#include <queue>
#include <thread>
#include<mutex>
#include<chrono>
#include<condition_variable>
#include<atomic>
#include<future>
using namespace std;
int total, max_size = 99999999, i;
promise<void> exitsignal;
future<void> futureObj;
int flagprod, cc, ff;
queue<int> ox;
mutex mtx, mtx1;
condition_variable cv;
//atomic <bool> noti
void push(int x) {
    unique_lock<mutex> lock(mtx);
    ox.push(x);
    /*if (ox.size() == max_size) {
        cv.wait(lock);
    }*/
}
bool pop(int &x) {
    
    if (ox.size() == 0) this_thread::sleep_for(chrono::milliseconds(1));
    unique_lock<mutex> lock(mtx);
    if (ox.size() != 0) {
        
        x = ox.front();
        ox.pop();

       // cv.notify_one();
        return true;
    }
    /*if (ox.size() == 0) {
        return false;
    }*/
    return false;
    
}
void producer() {
    for (int i = 0; i < 100000; i++) {
        push(1);
    }
    ff--;
    
}
void consumer() {
    int sum = 0;
    
    while (ff> 0 || ox.size()>0 ) {
        cout << "";
        int k;
        if (pop(k)) sum += k;
    }
    total += sum;

}
void task1(int count) {
    total = 0;
    size_t start = clock();
    vector<thread> producers(count);
    vector<thread> consumers(count);
    ff = count;
    for (int i = 0; i < count; i++) {
        producers[i] = thread(producer);
        consumers[i] = thread(consumer);
    }
    for (int i = 0; i < count; i++) {
        producers[i].join();
        consumers[i].join();
    }
    cout << "sum: " << total << " sum == all tasks: " << (total == 1024 * 1024 * 4 * count) << " Threads: " << count << " Time: " << (double)((clock() - start) / 1000.0) << " Queue size: " << ox.size() << endl;
}

int main()
{
    task1(1);
    task1(2);
    task1(4);
    cout << ((rand() % 2) == 1);
}

