#include "stack.hpp"

#include <iostream>

void Stack::add(int n)
{
    if (index + 1 == size)
        resize();
    data[index + 1] = n;
    index++;
}

int Stack::pop()
{
    index--;
    return data[index + 1];
}
