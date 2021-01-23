#include <iostream>
#include <string>

#include <gtest/gtest.h>

#include "factorial.hpp"

TEST(FactorialTest, ExpectedResults)
{
    ASSERT_EQ(factorial(1), 1);
    ASSERT_EQ(factorial(2), 2);
    ASSERT_EQ(factorial(3), 6);
    ASSERT_EQ(factorial(4), 24);
    ASSERT_EQ(factorial(5), 120);
}

TEST(FactorialTest, ErrorCheck)
{
    ASSERT_NE(factorial(1), 0);
    ASSERT_NE(factorial(2), 0);
    ASSERT_NE(factorial(3), 0);
    ASSERT_NE(factorial(4), 0);
    ASSERT_NE(factorial(5), 0);
}

TEST(FactorialTest, ThrowCheck)
{
    EXPECT_THROW(factorial(0), const char *);
}


int main(int argc, char** argv) {
    testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
