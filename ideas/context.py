import os
from .spec import Spec
from .entity import Entity

class Context:
	"""Entities which inherit the Context class are bound to implement methods
	   that facilitate interaction with entities, within contexts of other entities"""

	# Properties
	usableChildEntities = [Spec.UNIVERSE, Spec.GALAXY, Spec.SYSTEM,
	                       Spec.PLANET, Spec.OCEAN, Spec.CONTINENT,
	                       Spec.TERRITORY, Spec.PROVINCE, Spec.CITY,
	                       Spec.VILLAGE, Spec.DISTRICT, Spec.STRUCTURE,
	                       Spec.ROOM]
	allowedChildEntities = []
	childDirectory = "entities"

	# Methods
	def find(self, key):
		"""Attempt to locate the given key and load its entity. Uses usableChildEntities as a whitelist. Returns that entity"""

		# Check if the key exists in the child directory
		entityPath = self.path + '/' + self.childDirectory + '/' + self.key
		if (not os.path.exists(entityPath)):
			raise FileNotFoundError("The entity '" + key + "' could not be found")

		# Load it into the correct entity (by checking what it is)
		entity = Entity(key, entityPath)
		entity.load()
		correctSpec = entity.getSpec()

		entity = self.initChildEntityFromSpec(key, spec)
		entity.load()

		# Return it
		return entity

	def add(self, key, spec):
		"""Create a new entity and update its path to the child directory. Use allowedChildEntities as a whitelist"""

		# Check if the key exists in the child directory
		entityPath = self.path + '/' + self.childDirectory + '/' + self.key
		if (os.path.exists(entityPath)):
			raise FileExistsError("The entity '" + key + "' already exists")

		# Check the requested spec is allowed
		if (spec not in self.allowedChildEntities):
			raise FileNotFoundError("The entity '" + self.spec.name + "' may not create child '" + spec.name + "'")

		# Create the entity!
		entity = Spec.initEntityFromSpec(spec, key, entityPath)
		entity.create()

	def update(self, key = None):
		"""Display the update menu for the key'd entity. If None supplied, dispay update for current context entity"""

	def delete(self, key = None):
		"""Delete the key'd entity. If None supplied, delete current entity"""

	def initEntityFromSpec(self, spec, key, path):
		"""Retrieve a new entity of a given child class, based on the spec. Not sure if this method belongs in this class"""
		# This method should ALWAYS need to be re-implemented. It should contain conditions for each other allowed entity.
		
		raise FileNotFoundError("Entity '" + spec.name + "' cannot be found!") # Change error type.... (custom errors?)

			


