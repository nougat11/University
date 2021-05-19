BUILD_DIR = build

# ----------------------------------------------------------------------------------------------------------------------

all: clean executor.o main.o
	g++ -pthread $(BUILD_DIR)/main.o $(BUILD_DIR)/algorithm.o -o ${BUILD_DIR}/program

main.o: build
	g++ -c -Wall --std=c++17 main.cpp -o $(BUILD_DIR)/main.o

executor.o: build
	g++ -c -Wall --std=c++17 algorithm.cpp -o $(BUILD_DIR)/algorithm.o

# ----------------------------------------------------------------------------------------------------------------------

tests: clean_tests all
	./run_tests.sh

clean_tests:
	rm -f out.txt

# ----------------------------------------------------------------------------------------------------------------------

build:
	mkdir -p "$(BUILD_DIR)"

clean:
	rm -rf $(BUILD_DIR)
