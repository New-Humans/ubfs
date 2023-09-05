import datetime
from ...place import Place
from ...spec import Spec
from .plane import Plane

class Multiverse(Place):
	"""Multiverse is the top level context class (besides maybe reality). A Multiverse is allowed to contain planes.

	Attributes
		allowedChildEntities    Entity spec types that can be created from this context
		spec                   Spec type of this Entity"""

	# Things that child class SHOULDNT need to redeclare
	
	# Things that a few child classes will need to redeclare
	allowedChildEntities = [Spec.PLANE]

	# Things every child class will want to redeclare
	spec = Spec.MULTIVERSE

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
		if (spec == spec.PLANE):
			plane = Plane(key, path)
			return plane

		raise ContextEntityConflictError("No matching child-entity for '" + self.getSpecString() + " with spec " + spec.name)

