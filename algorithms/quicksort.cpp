#include <iostream>
#include <vector>

int partition(std::vector<int>& Q, int low, int high)
{
   int pivot = Q[low];
   int start = low;
   for(int i = low + 1; i <= high; i++)
   {
      if (Q[i] < pivot)
      {
         start++;
         std::swap(Q[start], Q[i]);
      }
   }
   std::swap(Q[start], Q[low]);
   return start;
}

void quicksort(std::vector<int>& Q, int low, int high)
{
   if (low < high)
   {
      int p = partition(Q, low, high);
      quicksort(Q, low, p - 1);
      quicksort(Q, p + 1, high);
   }
}

int main()
{
   std::vector<int> V(5);
   V[0] = 15;
   V[3] = 5;
   for (int i = 0; i < V.size(); i++)
   {
      std::cout << "Position " << i << ": " << V[i] << std::endl;
   }
   std::vector<int> U{3,7,5,2,8,6,4};
   quicksort(U, 0, U.size() - 1);
   for (int i = 0; i < U.size(); i++)
   {
      std::cout << U[i] << std::endl;
   }

   return 0;
}
