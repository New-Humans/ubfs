import datetime
from ...place import Place
from ...spec import Spec
from .room import Room
from ...person import Person

class Structure(Place):
	"""Structures can exist in many places. A structure is just a building of sorts. Other classes can import this.
	   Structures can contain rooms...

	Attributes
		allowedChildEntities    Entity spec types that can be created from this context
		spec                   Spec type of this Entity"""

	# Things that child class SHOULDNT need to redeclare
	
	# Things that a few child classes will need to redeclare
	allowedChildEntities = [Spec.ROOM, Spec.PERSON]

	# Things every child class will want to redeclare
	spec = Spec.STRUCTURE

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
		if (spec == spec.ROOM):
			room = Room(key, path)
			return room
		if (spec == spec.PERSON):
			person = Person(key, path)
			return person

		raise ContextEntityConflictError("No matching child-entity for '" + self.getSpecString() + " with spec " + spec.name)

