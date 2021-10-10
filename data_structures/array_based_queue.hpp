#pragma once

#include "dynamic_set.hpp"

class ArrayBasedQueue : DynamicSet
{
public:
    ArrayBasedQueue();
    ~ArrayBasedQueue() = default;

    void add(int n);
    int pop();

private:
    int add_index;
};