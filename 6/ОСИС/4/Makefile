BUILD_DIR = build
TESTS_DIR = tests

# ----------------------------------------------------------------------------------------------------------------------

all: build
	g++ main.cpp algorithm.cpp -o ${BUILD_DIR}/program -Wall

main:
	g++ main.cpp -o ${BUILD_DIR}/main -Wall

algorithm:
	g++ algorithm.cpp -o ${BUILD_DIR}/algorithm -Wall

# ----------------------------------------------------------------------------------------------------------------------

tests: clean_tests all
	./run_tests.sh

clean_tests:
	rm -f ${TESTS_DIR}/out[0123456789]*.txt

# ----------------------------------------------------------------------------------------------------------------------

build:
	mkdir build

clean: clean_tests
	rm -rf build
