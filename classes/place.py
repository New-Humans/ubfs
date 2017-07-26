from .context import Context
from .spec import Spec

class Place(Context):
	"""Places are all contexts by nature. Not many shared properties besides!

	Attributes
		bool isPlace    Overridden from Entity
		Spec spec       Overridden from Entity"""

	# Things that child class SHOULDNT need to redeclare
	isPlace = True
	spec = Spec.PLACE

	# ---- Methods ---- #
