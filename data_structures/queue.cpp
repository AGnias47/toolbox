#include "queue.hpp"

Queue::Queue() : DynamicSet()
{
    add_index = 0;
}

void Queue::add(int n)
{
    if (add_index == index || ((add_index) == size && index == 0))
    {
        add_index = size;
        resize();
    }
    if ((add_index) == size && index != 0)
        add_index = 0;
    if (index == -1)
        index = 0;
    data[add_index] = n;
    add_index++;
}

int Queue::pop()
{
    index++;
    return data[index - 1];
}
