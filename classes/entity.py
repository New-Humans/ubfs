import datetime
import os
import yaml
from .spec import Spec


class Entity:
	"""Anything that ever physically existed can be considered an entity.

	This class acts as a parent for the thing and context classes. In practice,
	general entities don't get created (nor are they fun or useful).

	Attributes (all private. Use getters/setters):
	    string key             Identifier for this entity. Constant once set.
	    Spec spec              Uses the Spec enum - public list of all entities.
	                           Should be overriden in each class to match the spec
	    string name            Name for the entity to be referred to as.
	    string description     General description of the entity.
	    date createdAt         Date and time of creation of the entity is stored.
	    date updatedAt         Keeps track of last time updated just for internal
	                           tracking. Uses the datetime package.
	    string path            Path from reality, to the directory containing this
	                           entity's YAML file. No trailing slash, directory
	                           shares a name with the entity key
	    string YAMLFileName    Name of .yaml file where entity data is serialized on save
	    string promptPrefix    Characters displayed previous to the askFor prompts
	    string promptSuffix    Characters displayed after the askFor prompts
	    bool isContext         Boolean specifying whether this entity could be treated
	                           as a context
	    bool isPerson          Boolean for determining if entity is person
	    bool isPlace           Boolean for determining if entity is a place
	    bool isThing           Boolean for determining if entity is a thing"""

	# Things that child classes SHOULDNT need to redeclare
	key = None
	name = None
	description = None
	createdAt = None
	updatedAt = None
	path = None
	YAMLFileName = "entity.yaml"

	# Things that a few child classes will need to redeclare
	isContext = False
	isPerson = False
	isPlace = False
	isThing = False
	promptPrefix = "> "
	promptSuffix = ": "

	# Things every child class will want to redeclare
	spec = Spec.ENTITY

	# ---- Methods ---- #
	# Constructor
	def __init__(self, key, path):
		"""Constructor for all entities.

		Do not redefine.

		Arguments
		string key     Identifier for this entity
		string path    Path relative to reality, including a trailing slash.

		Return
		None"""
		self.setKey(key)
		self.setPath(path + key)


	# Public methods
	def create(self):
		"""After construction, take the path and create this entity.

		Do not redefine.

		throws EntityAlreadyExistsError.

		Arguments
		None

		Return
		None"""

		# Error check to see if it already exists
		if (os.path.exists(self.getPath())):
			raise EntityAlreadyExistsError("Cannot create " + self.getSpecString() + " with key '" + self.getKey() + "'. Key already exists")

		# Tick the timestamps checkbox
		self.setCreatedAt(datetime.datetime.now())
		self.setUpdatedAt(datetime.datetime.now())

		# Create the entity's directory environment
		self.createDirectories()

		# Create the entity's YAML file
		self.createYAML()

		# Display the update menu to the user
		self.update()

	def load(self):
		"""After construction, take the path and YAMLFileName and attempt to load an existing entity.

		Do not redefine.

		Throws EntityNotFoundError.

		Arguments
		None

		Return
		None"""

		# Make sure the entity exists
		if (not os.path.exists(self.getPath() + '/' + self.getYAMLFileName())):
			raise EntityNotFoundError("Cannot load " + self.getSpecString() + " with key '" + self.getKey() + "'. Key not found")

		# Load the YAML file into memory
		self.loadYAML()


	def delete(self):
		"""After construction, take the path and attempt to delete the YAMLFileName there.

		Do not redefine.

		Throws EntityNotFoundError.

		Arguments
		None

		Return
		None"""

		# Make sure the entity exists
		if (not os.path.exists(self.getPath() + '/' + self.getYAMLFileName())):
			raise EntityNotFoundError("Cannot delete " + self.getSpecString() + " with key '" + self.getKey() + "'. Key not found")

		# End it all
		self.deleteYAML()

	def update(self):
		"""Display and handle interaction for a menu that updates this entity's properties.
		
		Should and will want to redefine.

		Arguments
		None

		Return
		None"""
		print("Editing %s '%s'" % (self.getSpecString(), self.getName()))
		choice = None
		while (choice != 3):
			choice = None 	
			while (choice != 1 and choice != 2 and choice != 3):
				print("Please select an action")
				print("  1) Edit name")
				print("  2) Edit description")
				print("  3) Save and continue navigating")
				choice = self.askForInteger("Action")

				if (choice != 1 and choice != 2 and choice != 3):
					print("Invalid choice!")

			if (choice == 1):
				self.setName(self.askForString("Please enter a name for this %s" % self.getSpecString()))
			elif (choice == 2):
				self.setDescription(self.askForString("Please enter a description for this %s" % self.getSpecString()))
			elif (choice == 3):
				print("Saving %s..." % self.getSpecString())
				self.setUpdatedAt(datetime.datetime.now())
				self.refreshYAML()
				print("Saved!")

	def dump(self):
		"""Dump key, spec, and path to console"""
		print("Key:  %s\nSpec: %s\nPath: %s" % (self.getKey(), self.getSpecString(), self.getPath()))


	def getIsContext(self):
		"""Return isContext attribute"""
		return self.isContext

	def getIsPerson(self):
		"""Return isPerson attribute"""
		return self.isPerson

	def getIsPlace(self):
		"""Return isPlace attribute"""
		return self.isPlace

	def getIsThing(self):
		"""Return isThing attribute"""
		return self.isThing


	# Private methods
	def createDirectories(self):
		"""Create directories needed for this entity. Called in create.

		Context will want to define. Unsure if any others.

		Arguments
		None

		Return
		None"""
		os.makedirs(self.getPath())

	def createYAML(self):
		"""Create the YAML file for this entity. Can't exist already.

		Do not redefine.

		Arguments
		None

		Return
		None"""
		
		# Check YAML doesn't already exist
		fullYAMLPath = self.getPath() + '/' + self.getYAMLFileName()
		if (os.path.exists(fullYAMLPath)):
			raise EntityAlreadyExistsError("Cannot create YAML for " + self.getSpecString() + " with key '" + self.getKey() + "'. YAML already exists")

		stream = open(fullYAMLPath, 'w')       # Open a new file stream
		entityDictionary = self.toYAML()       # Grab our entity definition
		yaml.dump(entityDictionary, stream)    # Dump the dictonary using the yaml package
		stream.close()

	def loadYAML(self):
		"""Load the serialized entity from its YAML file into its properties.

		Do not redefine.

		Arguments
		None

		Return
		None"""
		
		# Check entity exists
		fullYAMLPath = self.getPath() + '/' + self.getYAMLFileName()
		if (not os.path.exists(fullYAMLPath)):
			raise EntityAlreadyExistsError("Cannot load YAML for" + self.getSpecString() + " with key '" + self.getKey() + "'. YAML not found")

		stream = open(fullYAMLPath, 'r')
		entityDictionary = yaml.load(stream,  Loader=yaml.CLoader)    # Load the serialized YAML into a dictionary using yaml package
		stream.close()
		self.fromYAML(entityDictionary)         # Load the dictionary into memory

	def deleteYAML(self):
		"""Delete the associated YAML file. Do not redefine."""
		
		# Check YAML exists
		fullYAMLPath = self.getPath() + '/' + self.getYAMLFileName()
		if (not os.path.exists(fullYAMLPath)):
			raise EntityNotFoundError("Cannot delete YAML for " + self.getSpecString() + " with key '" + self.getKey() + "'. YAML not found")

		os.remove(fullYAMLPath)

	def refreshYAML(self):
		"""Update the YAML file with what's in the entity memory. Do not redefine"""
		self.deleteYAML()
		self.createYAML()

	def toString(self):
		"""Represent the entity attributes as a string.

		Will redefine on many entities

		Arguments
		None

		Return
		string"""
		# s = "The %s '%s':\n\n" % (self.getSpecString(), self.getName())
		s += "%s\n\n" % (self.getDescription())
		return s

	def toYAML(self):
		"""Convert the entity's attributes to a python dictionary.
		
		Will redefine often, probably.

		Arguments
		None

		Return
		Dictionary"""
		return {
			"key": self.getKey(),
			"spec": self.getSpec(),
			"name": self.getName(),
			"description": self.getDescription(),
			"createdAt": self.getCreatedAt().strftime("%Y-%m-%d %H:%M:%S.%f"),
			"updatedAt": self.getUpdatedAt().strftime("%Y-%m-%d %H:%M:%S.%f"),
		}

	def fromYAML(self, entityDict):
		"""Convert a python dictionary's values to our entity's attributes.

		Will redefine often, probably.

		Arguments
		Dictionary entityDict

		Return
		None"""
		self.setSpec(entityDict['spec'])
		self.setName(entityDict['name'])
		self.setDescription(entityDict['description'])
		self.setCreatedAt(datetime.datetime.strptime(entityDict['createdAt'], "%Y-%m-%d %H:%M:%S.%f"))
		self.setUpdatedAt(datetime.datetime.strptime(entityDict['updatedAt'], "%Y-%m-%d %H:%M:%S.%f"))

	def askForString(self, prompt):
		"""Gaurantee a string response to a prompt. Uses prefix and suffix attributes.

		Do not redefine.

		Arguments
		string prompt

		Return
		string"""
		return input(self.promptPrefix + prompt + self.promptSuffix)

	def askForInteger(self, prompt):
		"""Gaurantee an integer response to a prompt. Uses prefix and suffix attributes.

		Do not redefine.

		Arguments
		string prompt

		Return
		string"""
		return int(input(self.promptPrefix + prompt + self.promptSuffix))

	def askForDocument(self, prompt):
		doc = input(self.promptPrefix + prompt + self.promptSuffix)
		doc = doc.replace("<br>", "\n")
		return doc

	# Getters and setters... Bottom of the barrel
	def getKey(self):
		"""Return entity key value"""
		return self.key

	def setKey(self, key):
		"""Set entity key value"""
		self.key = key

	def getSpec(self):
		"""Return entity spec value"""
		return self.spec

	def getSpecString(self):
		"""Return string representation of entity spec value"""
		return self.spec.name

	def setSpec(self, spec):
		"""Set entity spec value"""
		self.spec = spec

	def getPath(self):
		"""Return path of entity"""
		return self.path

	def setPath(self, path):
		"""Set entity path value"""
		self.path = path

	def getName(self):
		"""Return friendly name of entity"""
		return self.name

	def setName(self, name):
		"""Set friendly name of entity"""
		self.name = name

	def getDescription(self):
		"""Return description of entity"""
		return self.description

	def setDescription(self, description):
		"""Set description for entity"""
		self.description = description

	def getYAMLFileName(self):
		"""Get YAMLFileName for the entity"""
		return self.YAMLFileName

	def getCreatedAt(self):
		"""Get created at for entity"""
		return self.createdAt

	def getCreatedAtString(self):
		"""Get created at string (not date object)"""
		return self.createdAt.strftime("%Y-%m-%d %H:%M")

	def setCreatedAt(self, date):
		"""Set created at attribute with datetime"""
		self.createdAt = date

	def getUpdatedAt(self):
		"""Get updated at for entity"""
		return self.updatedAt

	def getUpdatedAtString(self):
		"""Get updated at string (not date object)"""
		return self.updatedAt.strftime("%Y-%m-%d %H:%M")

	def setUpdatedAt(self, date):
		"""Set updated at attribute with datetime"""
		self.updatedAt = date

# Entities can throw a number of exceptions
class EntityAlreadyExistsError(Exception):
	pass
	
class EntityNotFoundError(Exception):
	pass
