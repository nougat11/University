#include<string>
#include<fstream>
#include"algorithm.h"
int main(int argc, char **argv) {
	std::string dirname = argv[1];
	std::string result_file= argv[2];
	std::ofstream f;
	f.open(result_file);
	f.close();
	thread_hub(dirname,result_file);

}
