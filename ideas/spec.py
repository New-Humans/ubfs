from enum import Enum

# How to keep track of what kind of an object a given entity
# is... types! Types should act as constants... for now.
# Type is a reserved word!
class Spec(Enum):
	ENTITY    = 1
	PERSON    = 2
	PLACE     = 3
	THING     = 4
	EXISTENCE = 5
	UNIVERSE  = 6
	GALAXY    = 7
	SYSTEM    = 8
	PLANET    = 9
	OCEAN     = 10
	CONTINENT = 11
	TERRITORY = 12
	PROVINCE  = 13
	CITY      = 14
	VILLAGE   = 15
	DISTRICT  = 16
	STRUCTURE = 17
	ROOM      = 18
