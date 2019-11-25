#include <stack>
#include <iostream>
#include <string>
#include <queue>

int main()
{
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
