#include "stack.hpp"
#include "queue.hpp"

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
    return 0;
}