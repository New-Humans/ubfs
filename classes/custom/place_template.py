from ..place import Place
from ..spec import Spec

class PlaceName(Place):
	"""[#Description]

	Attributes
		[#Attributes]"""

	# Things that child class SHOULDNT need to redeclare
	
	# Things that a few child classes will need to redeclare
	allowedChildEntites = []

	# Things every child class will want to redeclare
	spec = Spec.PLACENAME

	# ---- Methods ---- #
	def update(self):
		"""Display and handle interaction for a menu that updates this entity's properties.
		
		Should and will want to redefine.

		Arguments
		None

		Return
		None"""
		pass

	def toString(self):
		"""Represent the entity attributes as a string.

		Will redefine on many entities

		Arguments
		None

		Return
		string"""
		pass

	def toYAML(self):
		"""Convert the entity's attributes to a python dictionary.
		
		Will redefine often, probably.

		Arguments
		None

		Return
		Dictionary"""
		pass

	def fromYAML(self, entityDict):
		"""Convert a python dictionary's values to our entity's attributes.

		Will redefine often, probably.

		Arguments
		Dictionary entityDict

		Return
		None"""
		pass

