#include <iostream>
#include <queue>
#include <set>
#include <stack>
#include <string>


int main()
{
   std::set<std::string> names;
   names.insert("Andy");
   names.insert("Cezanne");
   names.insert("Dali");
   std::cout << "Is Andy in the set? \n";
   std::cout << names.count("Andy") << std::endl;
   std::cout << "Is Eton in the set?\n";
   std::cout << names.count("Eton") << std::endl;

   std::set<std::string>::iterator position;
   for (position = names.begin(); position != names.end(); position++)
   {
      std::cout << *position << std::endl;
   }

   std::stack<std::string> s;
   s.push("Booker");
   s.push("T");
   s.push("Washington");

   while (s.size() != 0 )
   {
      std::cout << s.top() << std::endl;
      s.pop();
   }

   std::queue<std::string> q;
   q.push("Booker");
   q.push("T");
   q.push("Washington");

   while (q.size() != 0)
   {
      std::cout << q.front() << std::endl;
      q.pop();
   }
   return 0;
}
