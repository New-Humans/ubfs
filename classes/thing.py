from .entity import Entity
from .spec import Spec

class Thing(Entity):
	"""Some things are contextual, some aren't. In this case, this thing isn't.

	Attributes
		bool isThing    Overridden from Entity
		Spec spec       Overridden from Entity"""

	# Things that child class SHOULDNT need to redeclare
	isThing = True
	spec = Spec.THING

	# ---- Methods ---- #
	