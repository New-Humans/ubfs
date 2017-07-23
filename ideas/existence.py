from .entity import Entity
from .context import Context
from .spec import Spec

class Existence(Entity, Context):
	"""Context basec entity which is the root of all other context. One per project"""

	# Existences must have (outside of base entity and context attributes...)
	spec = Spec.EXISTENCE

	# Existences should handle the following methods a little differently


	# Existences should be able to do this, custom-ly
