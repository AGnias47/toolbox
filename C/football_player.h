#ifndef ATHLETE_H
#define ATHLETE_H


/*
   Defines the Athlete structure. Properties include:
      name:        athlete's name as a string
      position:    athlete's position as a string
      number:      athlete's number as an int
      touchdowns:  athlete's touchdown count as an int
      quarterback: Athlete struct corresponding to the player's quarterback
*/
struct Athlete
{
   char* name;
   char* position;
   int number;
   int touchdowns;
   struct Athlete *quarterback;
};


/*
   Creates an athelete using all parameters
   @param _name:       string
   @param _position:   string
   @param _number:     int
   @param _touchdowns: int
   @param qb:          Athlete
   @return:            Athlete
*/
struct Athlete *create_athlete(char *_name, char *_position, int _number, int _touchdowns, struct Athlete *qb);


/*
   Creates an athelete using all parameters except the quarterback parameter
   @param _name:       string
   @param _position:   string
   @param _number:     int
   @param _touchdowns: int
   @return:            Athlete
*/
struct Athlete *create_athlete_no_qb(char *_name, char *_position, int _number, int _touchdowns);


/*
   Destroys an Athlete. Assumes if quarterback is defined, it exists outside of the scope of the 
   athlete being destroyed, i.e. create qb and then allocate to athlete as opposed to creating 
   the quarterback during initialization.
   @param _ath: Athlete
   @return:     None; _ath is destroyed
*/
void destroy_athlete(struct Athlete *_ath);

#endif
