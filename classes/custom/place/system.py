import datetime
from ...place import Place
from ...spec import Spec
from .planet import Planet
from .dwarfplanet import DwarfPlanet

class System(Place):
	"""Systems exist within galaxies, and can contain planets...

	Attributes
		allowedChildEntities    Entity spec types that can be created from this context
		spec                   Spec type of this Entity"""

	# Things that child class SHOULDNT need to redeclare
	
	# Things that a few child classes will need to redeclare
	allowedChildEntities = [Spec.PLANET, Spec.DWARFPLANET]

	# Things every child class will want to redeclare
	spec = Spec.SYSTEM

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
		if (spec == spec.PLANET):
			planet = Planet(key, path)
			return planet
		if (spec == spec.DWARFPLANET):
			dwarfPlanet = DwarfPlanet(key, path)
			return dwarfPlanet

		raise ContextEntityConflictError("No matching child-entity for '" + self.getSpecString() + " with spec " + spec.name)

