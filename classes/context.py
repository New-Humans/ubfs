import os
import yaml
import datetime
from .entity import Entity
from .entity import EntityNotFoundError
from .entity import EntityAlreadyExistsError
from .spec import Spec
from .colors import Colors

class Context(Entity):
	"""Contexts are entities of which other entities can exist within.

	This class acts as a parent primarily for Person(s) and Place(s). The
	difference between entities and contexts is the implementation of a child
	directory for child entities, and additional operations for adding and
	interacting with the child entities.

	Attributes (all private, use getters/setters)
	    Spec[] allowedChildEntities    List of specs that one is allowed to host
	                                   within this context
	    string childDirectory          String name for the child  directory
	    Spec spec                      Overridden from Entity
	    isContext                      Overridden from Entity"""

	# Things that child classes SHOULDNT need to redeclare
	isContext = True
	childDirectory = "e"

	# Things that every child class will want to redeclare
	spec = Spec.CONTEXT
	allowedChildEntities = []

	# ---- Methods ---- #
	# Public
	def find(self, key):
		"""Attempt to locate, load, and return an entity with the specified key in this context.

		Do not redefine.

		Arguments
		key    Key of entity to find

		Return
		Entity"""
		
		# Check if the queried entity exists
		entityPath = self.getPath() + '/' + self.getChildDirectory() + '/'
		if (not os.path.exists(entityPath + key)):
			raise EntityNotFoundError("Cannot locate entity with key '" + key + "' in " + self.getSpecString())

		# Load it into correct entity
		entity = Entity(key, entityPath)
		entity.load()
		correctSpec = entity.getSpec()
		entity = self.initEntityFromSpec(correctSpec, key, entityPath)
		entity.load()

		return entity

	def add(self, key, spec):
		"""Attempt to add given spec-type entity, with key, to this context.

		Do not redefine.

		Arguments
		key     Key of entity to add
		spec    Spec type for entity to add. Must match allowedChildren

		Return
		None"""
		
		# Make sure the entity doesn't already exist
		entityPath = self.getPath() + '/' + self.getChildDirectory() + '/'
		if (os.path.exists(entityPath + key)):
			raise EntityAlreadyExistsError("Can't add entity with key '" + key + "' to " + self.getSpecString())

		# Check allowed specs
		if (spec not in self.allowedChildEntities):
			raise ContextEntityConflictError("Can't add entity with key '" + key + "', type '" + spec.name + "' to " + self.getSpecString())

		# Create the new entity
		entity = self.initEntityFromSpec(spec, key, entityPath)
		entity.create()

	def toString(self):
		"""Represent the entity attributes as a string.

		Will redefine on many entities

		Arguments
		None

		Return
		string"""
		s = "%s\n\n" % (self.getDescription())
		s += "Contains:\n"
		if (not self.getContextualChildren()):
			s += " * There is nothing here...."
		# todo, get longest character length for: spec name, name, key, then use those as padding +1
		for entity in self.getContextualChildren():
			s += (" * "+Colors.OKBLUE+Spec.padString("<"+entity.getSpecString().upper()+">", 15)+Colors.ENDC)
			s += (Colors.OKCYAN+Spec.padString(entity.getName(), 20)+Colors.ENDC)
			s += (Colors.OKGREEN+"("+entity.getKey()+")"+Colors.ENDC+"\n")
			#s += (" * "+Colors.OKBLUE+Spec.padString("<%s>", 15)+Colors.ENDC+Colors.OKCYAN+" %s"+Colors.ENDC+Colors.OKGREEN+" (%s)"+Colors.ENDC+"\n") % (entity.getSpecString().upper(), entity.getName(), entity.getKey())
		return s

	# Private
	def initEntityFromSpec(self, spec, key, path):
		"""Attempt to initialize a specific entity using the spec type.

		Will likely redefine in Places.

		Arguments
		spec    Spec type for new entity
		key     Key for new entity
		path    Path for new entity

		Return
		Entity"""
		raise ContextEntityConflictError("Can't find entity with spec '" + spec.name + "' in this " + self.getSpecString())

	def getContextualChildren(self):
		"""Return list of entities, representing contextual children. Do not redefine."""
		childEntities = []
		for dirpaths, dirnames, filenames in os.walk(self.path + '/' + self.childDirectory):
			for key in dirnames:
				try:
					entity = Entity(key, self.path + '/' + self.childDirectory + '/')
					entity.load()
					correctSpec = entity.getSpec()
					entity = self.initEntityFromSpec(correctSpec, key, self.path + '/' + self.childDirectory + '/')
					entity.load()
					childEntities.append(entity)
				except EntityNotFoundError:
					pass # Skip entities which no longer exist...

		return childEntities

	def createDirectories(self):
		"""Create directories needed for this context. Called in create.

		Overridden from Entity. Children shouldn't override.

		Arguments
		None

		Return
		None"""
		os.makedirs(self.getPath())
		os.makedirs(self.getPath() + '/' + self.getChildDirectory())

	# Getters and setters...
	def getChildDirectory(self):
		"""Return context child directory string"""
		return self.childDirectory

	def setChildDirectory(self, dir):
		"""Set context child directory string"""
		self.childDirectory = dir

# Contexts can throw a number of exceptions
# For when adding entities that aren't allowed to contexts
class ContextEntityConflictError(Exception):
	pass


