from .entity import Entity
from .context import Context
from .spec import Spec
from .universe import Universe

class Existence(Entity, Context):
	"""Context basec entity which is the root of all other context. One per project"""

	# Existences must have (outside of base entity and context attributes...)
	spec = Spec.EXISTENCE
	allowedChildEntities = [Spec.UNIVERSE]

	# Existences should handle the following methods a little differently
	def initEntityFromSpec(self, spec, key, path):
		"""Retrieve a new entity of a given child class, based on the spec. Not sure if this method belongs in this class"""
		if (spec == Spec.UNIVERSE):
			return Universe(key, path)

		raise FileNotFoundError("Entity '" + spec.name + "' cannot be found!")

	# Existences should be able to do this, custom-ly
