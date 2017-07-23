import os
from .spec import Spec
from .entity import Entity
from .errors import EntityKeyNotFoundError, EntityIsNotAContextError, EntityAlreadyExistsError, IllogicalEntityError, InvalidSpecStringError


class Context:
	"""Entities which inherit the Context class are bound to implement methods
	   that facilitate interaction with entities, within contexts of other entities"""

	# Properties
	# Static (don't re-implement)
	usableChildEntities = [Spec.UNIVERSE, Spec.GALAXY, Spec.SYSTEM,
	                       Spec.PLANET, Spec.OCEAN, Spec.CONTINENT,
	                       Spec.TERRITORY, Spec.PROVINCE, Spec.CITY,
	                       Spec.VILLAGE, Spec.DISTRICT, Spec.STRUCTURE,
	                       Spec.ROOM]
	childDirectory = "entities"
	# Please re-implement
	allowedChildEntities = []
	

	# Methods
	def find(self, key, useFlag = False):
		"""Attempt to locate the given key and load its entity. Uses usableChildEntities as a whitelist. Returns that entity.
		   If the second argument useFlag is set to true, the useable child entities list is applied against the ID'd entity."""

		# Check if the key exists in the child directory
		entityPath = self.path + '/' + self.childDirectory + '/'
		if (not os.path.exists(entityPath + key)):
			raise FileNotFoundError("The entity '" + key + "' could not be found")

		# Load it into the correct entity (by checking what it is)
		entity = Entity(key, entityPath)
		entity.load()
		correctSpec = entity.getSpec()

		# Check it if necessary
		if (useFlag):
			if (correctSpec not in self.usableChildEntities):
				raise EntityIsNotAContextError("The useFlag was set, but the selected entity (" + entity.spec.name + ") is not a useable context!")

		# Load the located entity, return it
		entity = self.initEntityFromSpec(correctSpec, key, entityPath)
		entity.load()
		
		# Return it
		return entity

	def add(self, key, spec):
		"""Create a new entity and update its path to the child directory. Use allowedChildEntities as a whitelist"""

		# Check if the key exists in the child directory
		entityPath = self.path + '/' + self.childDirectory + '/'
		if (os.path.exists(entityPath + key)):
			raise FileExistsError("The entity '" + key + "' already exists")

		# Check the requested spec is allowed
		if (spec not in self.allowedChildEntities):
			raise IllogicalEntityError("The entity '" + self.spec.name + "' may not create child '" + spec.name + "'")

		# Create the entity!
		entity = self.initEntityFromSpec(spec, key, entityPath)
		entity.create()

	def update(self, key = None):
		"""Display the update menu for the key'd entity. If None supplied, dispay update for current context entity"""

	def delete(self, key = None):
		"""Delete the key'd entity. If None supplied, delete current entity"""

	def help(self):
		"""Return a string containing help information for this context"""
		# https://stackoverflow.com/a/10660443
		s = ("# Context Help\n\n"
			 "## Properties\n"
			 "Allowed child entities:\n"
			)

		for spec in self.allowedChildEntities:
			s += spec.name + "\n"

		s += "\nUseable child entities:\n"

		for spec in self.usableChildEntities:
			if spec in self.allowedChildEntities:
				s += spec.name + "\n"

		s += ("\n\n## Commands\n"
			 "HELP               Shows this menu. Help menus will change depending on\n"
			 "                   how different contexts work.\n"
			 "USE [key]          Move the frame of reference to a new context.\n"
			 "                   [key] is the unique key for a child of the current context.\n"
			 "BACK               Move back a frame of reference in the context stack.\n"
			 "                   One cannot move further back than existence.\n"
			 "SHOW [entity key]  Display information about a given entity. If\n"
			 "                   no key is supplied, the current frame of reference is used.\n"
			 "ADD [type] [key]   Create a new entity with a specific key. May trigger\n"
			 "                   some requests for input. Only allowed child entity types\n"
			 "                   may be created.\n"
			 "EDIT [key]         Bring up the editing menu for the selected entity.\n"
			 "                   If no key is provided, the current frame of reference is edited."
			)

		return s


	def initEntityFromSpec(self, spec, key, path):
		"""Retrieve a new entity of a given child class, based on the spec. Not sure if this method belongs in this class"""
		# This method should ALWAYS need to be re-implemented. It should contain conditions for each other allowed entity.
		
		raise FileNotFoundError("Entity '" + spec.name + "' cannot be found!") # Change error type.... (custom errors?)


	def getContextualChildren(self):
		"""Returns a list of entities. Entities correspond to nested children of this context"""
		pass


