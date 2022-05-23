cmake_minimum_required(VERSION 3.0)

project(GoogleTestExample)

find_package(GTest REQUIRED)
include_directories(${GTEST_INCLUDE_DIRS})

add_executable(gtest factorial.cpp test.cpp)
target_link_libraries(gtest ${GTEST_LIBRARIES} pthread)

add_test(NAME FactorialTest COMMAND gtest)
enable_testing()

