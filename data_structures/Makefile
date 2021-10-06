.PHONY: run_test clean all

C_COMPILER = gcc
COMPILER = g++

node: node.c
	${C_COMPILER} -o node node.c

dynamic_set: dynamic_set.cpp
	$(COMPILER) -c dynamic_set.cpp -o dynamic_set.o

stack: stack.cpp
	$(COMPILER) -c stack.cpp -o stack.o

queue: queue.cpp
	$(COMPILER) -c queue.cpp -o queue.o

linked_list: linked_list.cpp
	$(COMPILER) -c linked_list.cpp -o linked_list.o

compile_test: test.cpp
	$(COMPILER) test.cpp stack.o queue.o dynamic_set.o linked_list.o -o test

run_test:
	./test

clean:
	git clean -dxf

all: node dynamic_set stack queue linked_list compile_test run_test clean
