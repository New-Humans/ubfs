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
	WARD			= 1016
	MULTIVERSE      = 1017
	PLANE           = 1018
	COUNTRY			= 1019

	# Person roles (10001 - 20000) (isPerson = true)

	# Thing and ContextualThings (20001 - 100000) (isThing = true)
	BOOKCASE        = 20001
	BOOK            = 20002
	PAGE            = 20003
	SHOPPINGLIST    = 20004

	@staticmethod
	def getSpecString():
		return {
			"entity": Spec.ENTITY,
			"context": Spec.CONTEXT,
			"person": Spec.PERSON,
			"place": Spec.PLACE,
			"thing": Spec.THING,
			"contextualthing": Spec.CONTEXTUALTHING,
			"universe": Spec.UNIVERSE,
			"galaxy": Spec.GALAXY,
			"system": Spec.SYSTEM,
			"planet": Spec.PLANET,
			"ocean": Spec.OCEAN,
			"continent": Spec.CONTINENT,
			"territory": Spec.TERRITORY,
			"province": Spec.PROVINCE,
			"city": Spec.CITY,
			"village": Spec.VILLAGE,
			"district": Spec.DISTRICT,
			"structure": Spec.STRUCTURE,
			"room": Spec.ROOM,
			"dwarfplanet": Spec.DWARFPLANET,
			"restaurant": Spec.RESTAURANT,
			"bookcase": Spec.BOOKCASE,
			"book": Spec.BOOK,
			"page": Spec.PAGE,
			"shoppinglist": Spec.SHOPPINGLIST,
			"ward": Spec.WARD,
			"multiverse": Spec.MULTIVERSE,
			"plane": Spec.PLANE,
			"country": Spec.COUNTRY
		}

	@staticmethod
	def getSpecFromString(s):
		# Key types
		specString = Spec.getSpecString()
		if s in specString:
			return specString.get(s)
		raise InvalidSpecStringError("The supplied string '" + s + "' could not be recognized as a spec!")

	@staticmethod
	def getStringFromSpec(s):
		# Value types
		specString = Spec.getSpecString()
		if s in specString.values():
			return list(specString.values()).index(s)
		raise InvalidSpecStringError("The supplied string '" + s + "' could not be recognized as a spec!")

	@staticmethod
	def keyToName(input_string):	    
	    words = input_string.split('_')	    
	    words = [word.capitalize() for word in words]	    
	    transformed_string = ' '.join(words)	    
	    return transformed_string

	@staticmethod
	def padString(input_string, length):
	    # Check if the input string is already longer or equal to the desired length
	    if len(input_string) >= length:
	        return input_string
	    else:
	        # Calculate the number of spaces needed for padding
	        spaces_needed = length - len(input_string)
	        
	        # Pad the string with spaces on the right
	        padded_string = input_string + ' ' * spaces_needed
	        
	        return padded_string

# Spec errors!
class InvalidSpecStringError(Exception):
	pass