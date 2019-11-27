#include <set>
#include <string>
#include <iostream>

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
   
   return 0;
}


