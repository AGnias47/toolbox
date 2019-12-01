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

struct Athlete *create_athlete(char *_name, char *_position, int _number, int _touchdowns, struct Athlete *qb);
struct Athlete *create_athlete_no_qb(char *_name, char *_position, int _number, int _touchdowns);
void destroy_athlete(struct Athlete *_ath);
