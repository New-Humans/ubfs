from enum import Enum

# How to keep track of what kind of an object a given entity
# is... types! Types should act as constants... for now.
# Type is a reserved word!
class Spec(Enum):
	ENTITY    = 1
	PERSON    = 2
	PLACE     = 3
	THING     = 4
	UNIVERSE  = 5
	GALAXY    = 6
	SYSTEM    = 7
	PLANET    = 8
	OCEAN     = 9
	CONTINENT = 10
	TERRITORY = 11
	PROVINCE  = 12
	CITY      = 13
	VILLAGE   = 14
	DISTRICT  = 15
	STRUCTURE = 16
	ROOM      = 17

