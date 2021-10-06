#include "dynamic_set.hpp"

DynamicSet::DynamicSet()
{
    index = -1;
    size = DEFAULT_SIZE;
    data = new int[size];
}

void DynamicSet::resize()
{
    int new_size = size * 2;
    int *new_data = new int[size * 2];
    for (int i = 0; i < size; i++)
    {
        new_data[i] = data[i];
    }
    delete data;
    data = new_data;
    size *= 2;
}
