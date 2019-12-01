#include <stdlib.h>
#include <stdio.h>


struct Athlete
{
	char* name;
	char* position;
	int number;
	int touchdowns;
	struct Athlete *quarterback;
};


struct Athlete *create_athlete(char *_name, char *_position, int _number, int _touchdowns, struct Athlete *qb)
{
	struct Athlete *ath = malloc(sizeof(struct Athlete));
	ath->name = _name;
	ath->position = _position;
	ath->number = _number;
	ath->touchdowns = _touchdowns;
	ath->quarterback = qb;
	return ath;
}

struct Athlete *create_athlete_no_qb(char *_name, char *_position, int _number, int _touchdowns)
{
	struct Athlete *ath = malloc(sizeof(struct Athlete));
	ath->name = _name;
	ath->position = _position;
	ath->number = _number;
	ath->touchdowns = _touchdowns;
	return ath;
}


void destroy_athlete(struct Athlete *_ath)
{
	if (_ath != NULL) free(_ath);
}

int main()
{
	struct Athlete *carson = create_athlete_no_qb("Carson Wentz", "QB", 11, 27);
	struct Athlete *darren = create_athlete("Darren Sproles", "RB", 43, 2, carson);
	printf("Name: %s\n", darren->name);
	printf("Position: %s\n", darren->position);
	printf("Number: %d\n", darren->number);
	printf("Touchdowns: %d\n", darren->touchdowns);
	printf("Quarterback: %s\n", darren->quarterback->name);
	destroy_athlete(darren);
	return 0;
}
