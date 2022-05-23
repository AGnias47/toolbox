.PHONY: run_test clean all

C_COMPILER = gcc
COMPILER = g++

node: node.c
	${C_COMPILER} -o node node.c

dynamic_set: dynamic_set.cpp
	$(COMPILER) -c dynamic_set.cpp -o dynamic_set.o

stack: stack.cpp
	$(COMPILER) -c stack.cpp -o stack.o

array_based_queue: array_based_queue.cpp
	$(COMPILER) -c array_based_queue.cpp -o array_based_queue.o

linked_list: linked_list.cpp
	$(COMPILER) -c linked_list.cpp -o linked_list.o

queue: queue.cpp
	$(COMPILER) -c queue.cpp -o queue.o

compile_test: test.cpp
	$(COMPILER) test.cpp stack.o array_based_queue.o dynamic_set.o linked_list.o queue.o -o test

run_test:
	./test

clean:
	git clean -dxf

all: node dynamic_set stack array_based_queue linked_list queue compile_test run_test
