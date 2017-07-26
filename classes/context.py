from .entity import Entity
from .spec import Spec

class Context(Entity):
	"""Contexts are entities of which other entities can exist within.

	This class acts as a parent primarily for Person(s) and Place(s). The
	difference between entities and contexts is the implementation of a child
	directory for child entities, and additional operations for adding and
	interacting with the child entities.

	Attributes (all private, use getters/setters)
	    Spec[] allowedChildEntities    List of specs that one is allowed to host
	                                   within this context
	    string childDirectory          String name for the child  directory
	    Spec spec                      Overridden from Entity
	    isContext                      Overridden from Entity"""

	# Things that child classes SHOULDNT need to redeclare
	isContext = True
	childDirectory = "entities"

	# Things that every child class will want to redeclare
	spec = Spec.Context
	allowedChildEntities = []

	# ---- Methods ---- #
	# Public
	def find(self, key):
		"""Attempt to locate, load, and return an entity with the specified key in this context.

		Do not redefine.

		Arguments
		key    Key of entity to find

		Return
		Entity"""
		pass

	def add(self, key, spec):
		"""Attempt to add given spec-type entity, with key, to this context.

		Do not redefine.

		Arguments
		key     Key of entity to add
		spec    Spec type for entity to add. Must match allowedChildren

		Return
		None"""
		pass

	# Private
	def initEntityFromSpec(self, spec, key, path):
		"""Attempt to initialize a specific entity using the spec type.

		Will likely redefine in Places.

		Arguments
		spec    Spec type for new entity
		key     Key for new entity
		path    Path for new entity

		Return
		Entity"""
		pass

	def getContextualChildren(self):
		"""Return list of entities, representing contextual children. Do not redefine."""
		pass

	def createDirectories(self):
		"""Create directories needed for this context. Called in create.

		Overridden from Entity. Children shouldn't override.

		Arguments
		None

		Return
		None"""
		pass
