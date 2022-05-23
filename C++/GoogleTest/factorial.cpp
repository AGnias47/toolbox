#include "factorial.hpp"

int factorial(int n)
{
    if (n < 0)
    {
        throw "Must be >= 0";
    }
    else if (n == 0 || n == 1)
    {
        return n;
    }
    else
    {
        return n * factorial(n - 1);
    }
}


int factorial(int n, std::vector<int>& M)
{
    if (n < 0)
    {
        throw "Must be >= 0";
    }
    else if (M[n] != 0)
    {
        return M[n];
    }
    else if (n == 0 || n == 1)
    {
        M[n] = 1;
        return 1;
    }
    else
    {
        M[n] = n * factorial(n - 1);
        return M[n];
    }
}

