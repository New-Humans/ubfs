from .entity import Entity
from .context import Context
from .spec import Spec

class Universe(Entity, Context):
	"""Context based entity"""

	# Universes must have
	spec = Spec.UNIVERSE

	# Universes should handle the following methods a little differently


	# Universes should be able to do this, custom-ly
