#pragma once
#include "dynamic_set.hpp"

class Stack : public DynamicSet
{
public:

    Stack() : DynamicSet() {}
    ~Stack() = default;

    void add(int n);
    int pop();
};
