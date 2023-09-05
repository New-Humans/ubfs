import datetime
from ...place import Place
from ...spec import Spec
from .province import Province
from .city import City
from .village import Village
from .structure import Structure
from .restaurant import Restaurant

class Country(Place):
	"""Countries exist on continents and can contain provinces, cities, villages, and structures...

	Attributes
		allowedChildEntities    Entity spec types that can be created from this context
		spec                   Spec type of this Entity"""

	# Things that child class SHOULDNT need to redeclare
	
	# Things that a few child classes will need to redeclare
	allowedChildEntities = [Spec.PROVINCE, Spec.CITY, Spec.VILLAGE, Spec.STRUCTURE, Spec.RESTAURANT]

	# Things every child class will want to redeclare
	spec = Spec.COUNTRY

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
		if (spec == spec.PROVINCE):
			province = Province(key, path)
			return province
		if (spec == spec.CITY):
			city = City(key, path)
			return city
		if (spec == spec.VILLAGE):
			village = Village(key, path)
			return village
		if (spec == spec.STRUCTURE):
			structure = Structure(key, path)
			return structure
		if (spec == Spec.RESTAURANT):
			restaurant = Restaurant(key, path)
			return restaurant

		raise ContextEntityConflictError("No matching child-entity for '" + self.getSpecString() + " with spec " + spec.name)

