#pragma once

#include "linked_list.hpp"

class Queue
{
public:
    Queue();
    ~Queue() = default;

    void add(int n);
    int pop();
private:
    LinkedList queue;
};