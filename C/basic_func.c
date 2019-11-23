/*
   basic_func.c - File demonstrating basic functionality
                  of C; useful for refresing common functions 
                  and C syntax"

   Libraries Used:
                  stdio.h - printf and scanf

   Inputs: User input required for some functions
   Return: None; printf statements for each function

   Compiled using gcc version 9.2.1 20191008 
   Vim 8.0, indent=3 spaces
*/


#include <stdio.h>


/*
   Prints and int, char, and string

   @param: None
   @return: None
*/
void printing()
{
   printf("%d is a number\n", 7);
   printf("%c is a char\n", 'c');
   char *string = "This";
   printf("%s is a string\n", string);
}


/*
   Examples of how iterators function

   @param: None
   @return: None
*/
void iterators()
{
   int n = 1;
   printf("%d %d\n", n++, n++);
}


/*
   Reads in and prints out an array

   @param: None; requires user input
   @return: None
*/
void read_array()
{
   int size = 3;
   int a[size], *p;
   printf("Enter %d numbers: ", size);
   for (p = a; p < a+size; p++) scanf("%d", p);
   for (p = a; p < a+size; p++) printf("%d", *p);
   printf("\n");
   printf("1 element past the size: %d\n", a[size]);
}


/*
   Swaps two integer variables

   @param a: reference to int
   @param b: reference to int
   @return: None; mutates each int
*/
void swap(int *a, int *b)
{
   int temp = *b;
   *b = *a;
   *a = temp;
}


int main()
{
   printf("---printing---\n");
   printing();
   printf("---iterators---\n");
   iterators();
   printf("---read_array---\n");
   read_array();
   printf("---swap---\n");
   int a = 42;
   int b = 47;
   printf("a is %d and b is %d\n",a,b);
   printf("Running swap function\n");
   swap(&a,&b);
   printf("a is now %d and b is now %d\n",a,b);
   return 0;
}
