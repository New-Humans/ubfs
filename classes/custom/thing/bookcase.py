from ...contextualthing import ContextualThing
from ...spec import Spec
from .book import Book
from .shoppinglist import ShoppingList

class Bookcase(ContextualThing):
	"""A bookcase can usually be found in rooms!

	Attributes
		"""

	# Things that child class SHOULDNT need to redeclare
	
	# Things that a few child classes will need to redeclare
	allowedChildEntities = [Spec.BOOK, Spec.SHOPPINGLIST]

	# Things every child class will want to redeclare
	spec = Spec.BOOKCASE

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
		if (spec == Spec.BOOK):
			book = Book(key, path)
			return book
		if (spec == Spec.SHOPPINGLIST):
			shoppinglist = ShoppingList(key, path)
			return shoppinglist

		raise ContextEntityConflictError("Can't find entity with spec '" + spec.name + "' in this " + self.getSpecString())

