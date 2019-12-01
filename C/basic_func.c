/*
   basic_func.c - File demonstrating basic functionality
                  of C; useful for refresing common functions 
                  and C syntax"

   Libraries Used:
                  stdio.h - printf and scanf
                  stdlib.h - free and malloc
                  time.h - timer

   Inputs: User input required for some functions
   Return: None; printf statements for each function

   Compiled using gcc version 9.2.1 20191008 
   Vim 8.0, indent=3 spaces
*/


#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "football_player.h"


/*pseudo bool type*/
typedef int Bool;
enum{false, true};


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


/*
   Shows how an array can function as a pointer

   @params: none
   @return: None
*/
void array_as_pointer()
{
   int A[5];
   int *p;
   *A = 12;
   *(A+3) = 5;
   for (p=A; p<A+(sizeof(A)/sizeof(A[0])); p++) printf("%d\n", *p);
}


/*
   Returns a reversed array of ints using a for loop
   @param A: array to reverse (not mutated)
   @param size: size of array
   @return R: reversed array
*/
int * reverse_array(int * A, int size)
{
   if (A == NULL) return A;
   int * R = malloc(sizeof(int) * size);
   for (int i=size-1, j=0; i >= 0; i--, j++)
   {
      R[j] = A[i];
   }
   return R;
}

/*
   Shows timer functionality
   @params: None
   @return: None
*/
void timer()
{
   clock_t before;
   double elapsed;
   before = clock();
   int twentyfive = 5*5;
   elapsed = clock() - before;
   /*printf("Program took %.3f seconds to run\n",
         elapsed/CLOCKS_PER_SEC);*/
}


/*
   Partition helper function for quicksort
   @params: Array of ints, low index, high index
   @return: Partition index
*/
int partition(int A[], int low, int high)
{
   int start = low;
   int pivot = A[low];
   for (int i = low; i <= high; i++)
   {
      if (A[i] < pivot)
      {
         start++;
         swap(&A[start], &A[i]);
      }
   }
   swap(&A[start], &A[low]);
   return start;
}


/*
   Sorts an array in place
   @params: Array of ints, low index, high index
   @return: None; array is mutated by sort function
*/
void quicksort(int A[], int low, int high)
{
   if (low < high)
   {
      int p = partition(A, low, high);
      quicksort(A, low, p-1);
      quicksort(A, p+1, high);
   }
}


char switch_int_to_char(int n)
{
   char c;
   switch(n)
   {
      case 1: case 2: case 3:
         c = 'A';
         break;
      case 4: case  5: case 6:
         c = 'B';
         break;
      case 7: case 8: case 9:
         c = 'C';
         break;
      case 10:
         c = 'D';
         break;
      default:
         c = 'E';
         break;
   }
   return c;
}


int main()
{
   printf("---printing---\n");
   printing();
   printf("---iterators---\n");
   iterators();
   /*printf("---read_array---\n");
   read_array();*/
   printf("---swap---\n");
   int a = 42;
   int b = 47;
   printf("a is %d and b is %d\n",a,b);
   printf("Running swap function\n");
   swap(&a,&b);
   printf("a is now %d and b is now %d\n",a,b);
   printf("---Arrays as pointers---\n");
   array_as_pointer();
   int rev[] = {21, 32, 43};
   int *B = reverse_array(rev, 3);
   for (int i=0; i < 3; i++) printf("%d\n", B[i]);
   printf("---Quicksort---\n");
   int sort_array[] = {81, 897, 84, 17, 4686, 15};
   quicksort(sort_array, 0, 5);
   for (int i=0; i < 6; i++) printf("%d, ", sort_array[i]);
   printf("\n");
   printf("---Switch Statement---\n");
   char aa = switch_int_to_char(2);
   printf("%c\n", aa);
   char d = switch_int_to_char(10);
   printf("%c\n", d);
   char e = switch_int_to_char(15);
   printf("%c\n", e);
   printf("---Football Player Struct---\n");
   struct Athlete *carson = create_athlete_no_qb("Carson Wentz", "QB", 11, 27);
   struct Athlete *darren = create_athlete("Darren Sproles", "RB", 43, 2, carson);
   printf("Name: %s\n", darren->name);
   printf("Position: %s\n", darren->position);
   printf("Number: %d\n", darren->number);
   printf("Touchdowns: %d\n", darren->touchdowns);
   printf("Quarterback: %s\n", darren->quarterback->name);
   destroy_athlete(darren);
   timer();
   return 0;
}

