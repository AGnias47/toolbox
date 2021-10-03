#pragma once

#include "dynamic_set.hpp"

class Queue : DynamicSet
{
public:
    Queue();
    ~Queue() = default;

    void add(int n);
    int pop();

private:
    int add_index;
};