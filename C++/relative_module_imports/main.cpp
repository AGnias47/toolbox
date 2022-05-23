/*
	Example of a main function with dependent functions located in a different file
*/

#include <iostream>
#include "functions.h"

int main(){
	print_hello();
	std::cout << std::endl;
	std::cout << "The factorial of 5 is " << factorial(5) << std::endl;
	return 0;
}
