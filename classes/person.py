from .context import Context
from .spec import Spec

class Person(Context):
	"""Persons are all contexts by nature. Person != human!

	Child classes of Person may be more interesting than the it.

	Attributes
		string species    Person's species
		string height     Person's height (should include units)
		string weight     Person's weight (should include units)
		Spec spec         Overridden from Entity"""

	# Things that child class SHOULDNT need to redeclare
	isPerson = True
	species = None
	height = None
	weight = None
	spec = Spec.PERSON

	# ---- Methods ---- #
	