#include "stack.hpp"
#include "array_based_queue.hpp"
#include "linked_list.hpp"

#include <assert.h>

#include <iostream>

void test_stack()
{
    Stack stack = Stack();
    stack.add(1);
    stack.add(3);
    stack.add(5);
    assert(stack.pop() == 5);
    assert(stack.pop() == 3);
    assert(stack.pop() == 1);
    for (int i = 0; i < 15000; i++)
    {
        stack.add(i);
    }
    for (int i = 14999; i > 0; i--)
    {
        assert(stack.pop() == i);
    }
    std::cout << "Stack test passed" << std::endl;
}

void test_queue()
{
    ArrayBasedQueue queue = ArrayBasedQueue();
    queue.add(1);
    queue.add(3);
    queue.add(5);
    assert(queue.pop() == 1);
    assert(queue.pop() == 3);
    assert(queue.pop() == 5);
    for (int i = 0; i < 15000; i++)
    {
        queue.add(i);
    }
    for (int i = 0; i < 15000; i++)
    {
        assert(queue.pop() == i);
    }
    std::cout << "Array-based Queue test passed" << std::endl;
}

void test_linked_list()
{
    LinkedList linked_list = LinkedList();
    linked_list.add_first(5);
    linked_list.add(0, 3);
    linked_list.add_first(1);
    linked_list.add_last(7);
    linked_list.add(4, 9);
    linked_list.add_first(0);
    assert(linked_list.retrieve(0) == 0);
    assert(linked_list.retrieve(1) == 1);
    assert(linked_list.retrieve(2) == 3);
    assert(linked_list.retrieve(3) == 5);
    assert(linked_list.retrieve(4) == 7);
    assert(linked_list.retrieve(5) == 9);
    assert(linked_list.first() == 0);
    assert(linked_list.last() == 9);
    linked_list.add(3, 4);
    linked_list.print_list();
    assert(linked_list.pop_first() == 0);
    assert(linked_list.pop_first() == 1);
    assert(linked_list.pop_first() == 3);
    assert(linked_list.pop_last() == 9);
    assert(linked_list.pop_last() == 7);
    linked_list.add_last(6);
    assert(linked_list.remove(1) == 5);
    assert(linked_list.search(5) == -1);
    assert(linked_list.search(6) == 1);
    linked_list.print_list();
}

int main()
{
    test_stack();
    test_queue();
    return 0;
}
