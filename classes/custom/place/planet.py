import datetime
from ...place import Place
from ...spec import Spec
from .ocean import Ocean
from .continent import Continent

class Planet(Place):
	"""Planets exist within systems. Planets are divided into oceans and continents...

	Attributes
		allowedChildEntities    Entity spec types that can be created from this context
		spec                   Spec type of this Entity"""

	# Things that child class SHOULDNT need to redeclare
	
	# Things that a few child classes will need to redeclare
	allowedChildEntities = [Spec.OCEAN, Spec.CONTINENT]
	isDwarfPlanet = False

	# Things every child class will want to redeclare
	spec = Spec.PLANET

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
		if (spec == spec.OCEAN):
			ocean = Ocean(key, path)
			return ocean
		if (spec == spec.CONTINENT):
			continent = Continent(key, path)
			return continent

		raise ContextEntityConflictError("No matching child-entity for '" + self.getSpecString() + " with spec " + spec.name)


	# Getters / Setters
	# Why can't I override variables and methods
	def getIsDwarfPlanet(self):
		return self.isDwarfPlanet