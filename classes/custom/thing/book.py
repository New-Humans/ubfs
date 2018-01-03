from ...contextualthing import ContextualThing
from ...spec import Spec
from .page import Page

class Book(ContextualThing):
	"""Books can have pages! Found in many places.

	Attributes
		Nothing much yet!"""

	# Things that child class SHOULDNT need to redeclare
	
	# Things that a few child classes will need to redeclare
	allowedChildEntities = [Spec.PAGE]

	# Things every child class will want to redeclare
	spec = Spec.BOOK

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
		if (spec == Spec.PAGE):
			page = Page(key, path)
			return page

		raise ContextEntityConflictError("Can't find entity with spec '" + spec.name + "' in this " + self.getSpecString())

