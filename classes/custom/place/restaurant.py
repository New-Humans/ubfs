from ...spec import Spec
from .structure import Structure

class Restaurant(Structure):
	"""Restaurants! Food n stuff :)

	Attributes
		allowedChildEntities    Entity spec types that can be created from this context
		spec                    Spec type of this Entity"""

	# Things that child class SHOULDNT need to redeclare
	
	# Things that a few child classes will need to redeclare

	# Things every child class will want to redeclare
	spec = Spec.RESTAURANT

	# ---- Methods ---- #
