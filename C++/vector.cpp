#include <iostream>
#include <vector>

int main()
{
	std::vector<int> V(5);
	V[0] = 15;
	V[3] = 5;
	for (int i = 0; i < V.size(); i++)
	{
		std::cout << "Position " << i << ": " << V[i] << std::endl;
	}

	return 0;
}
