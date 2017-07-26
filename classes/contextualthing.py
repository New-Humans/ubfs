from .context import Context
from .spec import Spec

class ContextualThing(Context):
	"""Some things are contextual, some aren't. In this case, this thing is.

	Attributes
		bool isThing    Overridden from Entity
		Spec spec       Overridden from Entity"""

	# Things that child class SHOULDNT need to redeclare
	isThing = True
	spec = Spec.THING

	# ---- Methods ---- #
	