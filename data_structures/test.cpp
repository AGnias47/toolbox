#include "stack.hpp"
#include "queue.hpp"
#include "linked_list.hpp"

#include <assert.h>

#include <iostream>

int main()
{
    Stack stack = Stack();
    stack.add(1);
    stack.add(3);
    stack.add(5);
    std::cout << stack.pop() << std::endl;
    std::cout << stack.pop() << std::endl;
    std::cout << stack.pop() << std::endl;

    Queue queue = Queue();
    queue.add(1);
    queue.add(3);
    queue.add(5);
    std::cout << queue.pop() << std::endl;
    std::cout << queue.pop() << std::endl;
    std::cout << queue.pop() << std::endl;

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

    return 0;
}
