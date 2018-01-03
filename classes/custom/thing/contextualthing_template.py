from ...contextualthing import ContextualThing
from ...spec import Spec

class ThingName(ContextualThing):
	"""[#Description]

	Attributes
		[#Attributes]"""

	# Things that child class SHOULDNT need to redeclare
	
	# Things that a few child classes will need to redeclare
	allowedChildEntities = []

	# Things every child class will want to redeclare
	spec = Spec.THINGNAME

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
		raise ContextEntityConflictError("Can't find entity with spec '" + spec.name + "' in this " + self.getSpecString())

