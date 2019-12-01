COMPILER = gcc
OUTFILE = "main"

build: basic_func node

basic_func: basic_func.c football_player.c
	${COMPILER} -o ${OUTFILE} basic_func.c football_player.c

node: node.c
	${COMPILER} -o node node.c
