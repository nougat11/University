#include<mutex>
#include<fstream>
#include"algorithm.h"
#include <vector>
#include <filesystem>
#include <iostream>
#include<thread>
std::mutex mtx;
void thread_hub(std::string dir, std::string result_file) {
	std::vector<std::thread> calc(100);
	int counter = 0;
	for (const auto& entry : std::filesystem::directory_iterator(dir)) {
		std::string path = entry.path().string();
		calc[counter++] = std::thread(calculation, path, result_file);
		std::cout << path << std::endl;
	}
	for (int i = 0; i < counter; i++) {
		calc[i].join();
	}
}
void calculation(std::string path, std::string result_file) {
	std::ifstream f;
	f.open(path);
	int operation;
	double number1, number2;
	f >> operation;
	f >> number1 >> number2;
	f.close();
	double result;
	switch (operation) {
	case 1:
		result = number1 + number2;
		break;
	case 2:
		result = number1 * number2;
		break;
	case 3:
		result = (number1 * number1) + (number2 * number2);
		break;
	default:
		result = 0;
	}
	mtx.lock();
	std::ofstream fout;
	fout.open(result_file, std::ios::app);
	fout << result << std::endl;
	mtx.unlock();


}
