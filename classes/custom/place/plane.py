import datetime
from ...place import Place
from ...spec import Spec
from .continent import Continent
from .ocean import Ocean
from .city import City
from .structure import Structure
from .galaxy import Galaxy
from .layer import Layer
from .system import System

class Plane(Place):
	"""Planes exist within multiverses, and can contain many things..

	Attributes
		allowedChildEntities    Entity spec types that can be created from this context
		spec                   Spec type of this Entity"""

	# Things that child class SHOULDNT need to redeclare
	
	# Things that a few child classes will need to redeclare
	allowedChildEntities = [Spec.PLANE, Spec.CONTINENT, Spec.OCEAN, Spec.CITY, Spec.STRUCTURE, Spec.GALAXY, Spec.LAYER, Spec.SYSTEM]

	# Things every child class will want to redeclare
	spec = Spec.PLANE

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
		if (spec == spec.CONTINENT):
			continent = Continent(key, path)
			return continent
		if (spec == spec.OCEAN):
			ocean = Ocean(key, path)
			return ocean
		if (spec == spec.CITY):
			city = City(key, path)
			return city
		if (spec == spec.STRUCTURE):
			structure = Structure(key, path)
			return structure
		if (spec == spec.GALAXY):
			galaxy = Galaxy(key, path)
			return galaxy
		if (spec == spec.PLANE):
			plane = Plane(key, path)
			return plane
		if (spec == spec.LAYER):
			layer = Layer(key, path)
			return layer
		if (spec == spec.SYSTEM):
			system = System(key, path)
			return system

		raise ContextEntityConflictError("No matching child-entity for '" + self.getSpecString() + " with spec " + spec.name)

