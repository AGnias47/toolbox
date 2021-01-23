#include "factorial.hpp"

int factorial(int n)
{
    if (n < 1)
    {
        throw "Must be > 0";
    }
    if (n == 1)
    {
        return n;
    }
    else
    {
        return n * factorial(n - 1);
    }
}

