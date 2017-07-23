from enum import Enum
from .errors import InvalidSpecStringError

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


	@staticmethod
	def getSpecFromString(s):
		if (s == "entity"):
			return Spec.ENTITY
		if (s == "person"):
			return Spec.PERSON
		if (s == "place"):
			return Spec.PLACE
		if (s == "thing"):
			return Spec.THING
		if (s == "existence"):
			return Spec.EXISTENCE
		if (s == "universe"):
			return Spec.UNIVERSE
		if (s == "galaxy"):
			return Spec.GALAXY
		if (s == "system"):
			return Spec.SYSTEM
		if (s == "planet"):
			return Spec.PLANET
		if (s == "ocean"):
			return Spec.OCEAN
		if (s == "continent"):
			return Spec.CONTINENT
		if (s == "territory"):
			return Spec.TERRITORY
		if (s == "province"):
			return Spec.PROVINCE
		if (s == "city"):
			return Spec.CITY
		if (s == "village"):
			return Spec.VILLAGE
		if (s == "district"):
			return Spec.DISTRICT
		if (s == "structure"):
			return Spec.STRUCTURE
		if (s == "room"):
			return Spec.ROOM

		raise InvalidSpecStringError("The supplied spec '" + s + "' could not be recognized!")

