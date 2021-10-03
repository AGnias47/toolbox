#pragma once

#define DEFAULT_SIZE 5000

class DynamicSet
{
public:
    int *data;
    int index;
    int size;

    DynamicSet();
    ~DynamicSet() = default;

    virtual void add(int n) = 0;
    virtual int pop() = 0;
    void resize();
};
