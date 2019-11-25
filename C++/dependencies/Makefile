.cpp.o:
	g++ -c $<

SOURCE = main.cpp hello.cpp factorial.cpp
OBJS = ${SOURCE:.cpp=.o}

main: $(OBJS)
	g++ -o main $(OBJS)
