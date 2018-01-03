from ...place import Place
from ...spec import Spec
from ..thing.bookcase import Bookcase

class Room(Place):
	"""A room is almost as low a place can go, probably. Rooms probably can't contain many other places, but lots of things!

	Attributes
		allowedChildEntities    Entity spec types that can be created from this context
		spec                   Spec type of this Entity"""

	# Things that child class SHOULDNT need to redeclare
	
	# Things that a few child classes will need to redeclare
	allowedChildEntities = [Spec.BOOKCASE]

	# Things every child class will want to redeclare
	spec = Spec.ROOM

	# ---- Methods ---- #
	def initEntityFromSpec(self, spec, key, path):
		"""Attempt to initialize a specific entity using the spec type.

		Will likely redefine in Places.

		Arguments
		spec    Spec type for new entity
		key     Key for new entity
		path    Path for new entity

		Return
		Entity"""
		if (spec == Spec.BOOKCASE):
			bookcase = Bookcase(key, path)
			return bookcase

		raise ContextEntityConflictError("No matching child-entity for '" + self.getSpecString() + " with spec " + spec.name)

