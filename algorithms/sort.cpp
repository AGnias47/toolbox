#include <iostream>
#include <limits>
#include <vector>

std::vector<int> insertion_sort(std::vector<int> V)
{
   for (int j = 1; j < V.size(); j++)
   {
      int key = V[j];
      int i = j - 1;
      while (i >= 0 && V[i] > key)
      {
         V[i + 1] = V[i];
         i--;
      }
      V[i + 1] = key;
   }
   return V;
}

void merge(std::vector<int> &V, int p, int q, int r)
{
   int left_last_index = q - p;
   int right_last_index = r - q - 1;
   std::vector<int> L(left_last_index + 2);
   std::vector<int> R(right_last_index + 2);
   for (int i = 0; i <= left_last_index; i++)
   {
      L[i] = V[p + i];
   }
   for (int i = 0; i <= right_last_index; i++)
   {
      R[i] = V[q + i + 1];
   }
   L[left_last_index + 1] = std::numeric_limits<int>::max();
   R[right_last_index + 1] = std::numeric_limits<int>::max();
   int i = 0;
   int j = 0;
   for (int k = p; k <= r; k++)
   {
      if (L[i] < R[j])
      {
         V[k] = L[i];
         i++;
      }
      else
      {
         V[k] = R[j];
         j++;
      }
   }
}

void merge_sort(std::vector<int> &V, int p, int r)
{
   if (p < r)
   {
      int q = (p + r) / 2;
      merge_sort(V, p, q);
      merge_sort(V, q + 1, r);
      merge(V, p, q, r);
   }
}

int partition(std::vector<int> &Q, int low, int high)
{
   int pivot = Q[low];
   int start = low;
   for (int i = low + 1; i <= high; i++)
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

void quicksort(std::vector<int> &Q, int low, int high)
{
   if (low < high)
   {
      int p = partition(Q, low, high);
      quicksort(Q, low, p - 1);
      quicksort(Q, p + 1, high);
   }
}

void print_vector(std::vector<int> V)
{
   for (int i = 0; i < V.size(); i++)
   {
      std::cout << V[i];
      if (i + 1 != V.size())
         std::cout << ", ";
   }
   std::cout << std::endl;
}

int main()
{
   std::vector<int> I{3, 7, 5, 2, 8, 6, 4};
   std::vector<int> M = I;
   std::vector<int> Q = I;

   std::vector<int> insertion_sort_results = insertion_sort(I);
   std::cout << "Insertion Sort Results" << std::endl;
   print_vector(insertion_sort_results);

   merge_sort(M, 0, M.size() - 1);
   std::cout << "Merge Sort Results" << std::endl;
   print_vector(M);

   quicksort(Q, 0, Q.size() - 1);
   std::cout << "Quicksort Results" << std::endl;
   print_vector(Q);
   return 0;
}
