#pragma once

#include <vector>

/** Recursive factorial function
  * @param n - Number to find factorial of */
int factorial(int n);

/** Recursive factorial function with memoization
  * @param n - Number to find factorial of 
  * @param M - Memoization vector                 
  * @return int                                   */
int factorial(int n, std::vector<int>& M);

