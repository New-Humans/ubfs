from ...spec import Spec
from .planet import Planet

class DwarfPlanet(Planet):
	"""Dwarf planets are a subclass of planet.

	Attributes
		allowedChildEntities    Entity spec types that can be created from this context
		spec                   Spec type of this Entity"""

	# Things that child class SHOULDNT need to redeclare
	
	# Things that a few child classes will need to redeclare
	isDwarfPlanet = True

	# Things every child class will want to redeclare
	spec = Spec.DWARFPLANET

	# ---- Methods ---- #
	def toString(self):
		"""Represent the entity attributes as a string.

		Will redefine on many entities

		Arguments
		None

		Return
		string"""
		s = "The dwarf planet '%s':\n\n" % (self.getName())
		s += "%s\n" % (self.getDescription())
		s += "Entities in this planet:\n"
		for entity in self.getContextualChildren():
			s += "  * [%s] The %s '%s'\n" % (entity.getKey(), entity.getSpecString(), entity.getName())
			
		return s
