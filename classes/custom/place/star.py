import datetime
from ...place import Place
from ...spec import Spec

class Star(Place):
	"""Stars exist within systems.

	Attributes
		allowedChildEntities    Entity spec types that can be created from this context
		spec                   Spec type of this Entity"""

	# Things that child class SHOULDNT need to redeclare
	
	# Things that a few child classes will need to redeclare
	allowedChildEntities = []
	isDwarfPlanet = False

	# Things every child class will want to redeclare
	spec = Spec.STAR

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

		raise ContextEntityConflictError("No matching child-entity for '" + self.getSpecString() + " with spec " + spec.name)
