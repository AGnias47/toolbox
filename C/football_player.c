#include <stdlib.h>
#include "football_player.h"


extern struct Athlete *create_athlete(char *_name, char *_position, int _number, int _touchdowns, struct Athlete *qb)
{
   struct Athlete *ath = malloc(sizeof(struct Athlete));
   ath->name = _name;
   ath->position = _position;
   ath->number = _number;
   ath->touchdowns = _touchdowns;
   ath->quarterback = qb;
   return ath;
}

extern struct Athlete *create_athlete_no_qb(char *_name, char *_position, int _number, int _touchdowns)
{
   struct Athlete *ath = malloc(sizeof(struct Athlete));
   ath->name = _name;
   ath->position = _position;
   ath->number = _number;
   ath->touchdowns = _touchdowns;
   return ath;
}


extern void destroy_athlete(struct Athlete *_ath)
{
   if (_ath != NULL) free(_ath);
}
