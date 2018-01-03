from enum import Enum

# How to keep track of what kind of an object a given entity
# is... types! Types should act as constants... for now.
# Type is a reserved word!
class Spec(Enum):
	# Key types (1-1000)
	ENTITY          = 1
	CONTEXT         = 2
	PERSON          = 3
	PLACE           = 4
	THING           = 5
	CONTEXTUALTHING = 6

	# Places (1001-10000) (isPlace = true)
	UNIVERSE        = 1001
	GALAXY          = 1002
	SYSTEM          = 1003
	PLANET          = 1004
	OCEAN           = 1005
	CONTINENT       = 1006
	TERRITORY       = 1007
	PROVINCE        = 1008
	CITY            = 1009
	VILLAGE         = 1010
	DISTRICT        = 1011
	STRUCTURE       = 1012
	ROOM            = 1013
	DWARFPLANET     = 1014
	RESTAURANT      = 1015

	# Person roles (10001 - 20000) (isPerson = true)

	# Thing and ContextualThings (20001 - 100000) (isThing = true)
	BOOKCASE        = 20001
	BOOK            = 20002
	PAGE            = 20003
	SHOPPINGLIST    = 20004

	@staticmethod
	def getSpecFromString(s):
		# Key types
		if (s == "entity"):
			return Spec.ENTITY
		if (s == "context"):
			return Spec.CONTEXT
		if (s == "person"):
			return Spec.PERSON
		if (s == "place"):
			return Spec.PLACE
		if (s == "thing"):
			return Spec.THING
		if (s == "contextualthing"):
			return Spec.CONTEXTUALTHING

		# Places
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
		if (s == "dwarfplanet"):
			return Spec.DWARFPLANET
		if (s == "restaurant"):
			return Spec.RESTAURANT

		# Persons

		# Things / ContextualThings
		if (s == "bookcase"):
			return Spec.BOOKCASE
		if (s == "book"):
			return Spec.BOOK
		if (s == "page"):
			return Spec.PAGE
		if (s == "shoppinglist"):
			return Spec.SHOPPINGLIST

		raise InvalidSpecStringError("The supplied string '" + s + "' could not be recognized as a spec!")


# Spec errors!
class InvalidSpecStringError(Exception):
	pass