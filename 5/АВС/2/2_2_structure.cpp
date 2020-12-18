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
void dynamic_push(int x) {
    unique_lock<mutex> lock(mtx);
    ox.push(x);
}
void fixed_push(int x) {
    unique_lock<mutex> lock(mtx);
    ox.push(x);
    if (ox.size() == max_size) {
        cv.wait(lock);
    }
}
void push(int x, bool TYPE) {
    if (TYPE) dynamic_push(x);
    else fixed_push(x);
}
bool dynamic_pop(int& x) {

    if (ox.size() == 0) this_thread::sleep_for(chrono::milliseconds(1));
    unique_lock<mutex> lock(mtx);
    if (ox.size() != 0) {
        x = ox.front();
        ox.pop();
        return true;
    }
    
    return false;
}
bool fixed_pop(int& x) {

    if (ox.size() == 0) this_thread::sleep_for(chrono::milliseconds(1));
    unique_lock<mutex> lock(mtx);
    if (ox.size() != 0) {
        x = ox.front();
        ox.pop();
        cv.notify_one();
        return true;
    }
    
    return false;

}
bool pop(int& x, bool TYPE) {
    if (TYPE) return dynamic_pop(x);
    return fixed_pop(x);
}




void producer(bool type) {
    for (int i = 0; i < 2000; i++) {
        push(1,type);
    }
    ff--;

}
void consumer(bool type) {
    int sum = 0;

    while (ff > 0 || ox.size() > 0) {
        cout << "";
        int k;
        if (pop(k, type)) sum += k;
    }
    total += sum;

}
void task(int count, bool TYPE, int size) {
    if (!TYPE) {
        max_size = size;
    }
    total = 0;
    size_t start = clock();
    vector<thread> producers(count);
    vector<thread> consumers(count);
    ff = count;
    for (int i = 0; i < count; i++) {
        producers[i] = thread(producer, TYPE);
        consumers[i] = thread(consumer, TYPE);
    }
    for (int i = 0; i < count; i++) {
        producers[i].join();
        consumers[i].join();
    }
    cout << "sum: " << total << " sum == all tasks: " << (total == 2000 * count) << " Threads: " << count << " Time: " << (double)((clock() - start) / 1000.0) << " Queue size: " << ox.size() << " MAX_SIZE: "<< max_size<< endl;
}

int main()
{
    task(1, true, 0);
    task(2, true, 0);
    task(4, true, 0);
    task(1, false, 1);
    task(2, false, 1);
    task(4, false, 1);
    task(1, false, 4);
    task(2, false, 4);
    task(4, false, 4);
    task(1, false, 16);
    task(2, false, 16);
    task(4, false, 16);
    
}

