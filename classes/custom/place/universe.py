import datetime
from ...place import Place
from ...spec import Spec
from .galaxy import Galaxy

class Universe(Place):
	"""Universe is the top level context class (besides maybe reality). A universe is allowed to contain galaxies.

	Attributes
		allowedChildEntities    Entity spec types that can be created from this context
		spec                   Spec type of this Entity"""

	# Things that child class SHOULDNT need to redeclare
	
	# Things that a few child classes will need to redeclare
	allowedChildEntities = [Spec.GALAXY]

	# Things every child class will want to redeclare
	spec = Spec.UNIVERSE

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
		if (spec == spec.GALAXY):
			galaxy = Galaxy(key, path)
			return galaxy

		raise ContextEntityConflictError("No matching child-entity for '" + self.getSpecString() + " with spec " + spec.name)

