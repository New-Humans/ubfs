import yaml
import datetime
import os

# Entity class for Universe builder
# EVERYTHING is an entity! Maybe (probably)!
class Entity:
	"""Encompessing parent class for all other UBFS objects"""

	# Properties
	name = None
	friendly = None
	description = None
	createdAt = None
	updatedAt = None
	directory = None
	entityFile = "entity_meta.yaml"
	promptPrefix = "> "
	promptSuffix = " "
	customProperties = {}

	# Actions
	def __init__(self, name):
		self.name = name
		self.createdAt = datetime.datetime.now()
		self.updatedAt = datetime.datetime.now()

	def setName(self, name):
		self.name = name

	def setDescription(self, description):
		self.description = description

	def setFriendly(self, friendly):
		self.friendly = friendly

	def setCustomProperty(self, key, value):
		self.customProperties[key] = value;

	def getCustomProperty(self, key):
		if (key in self.customProperties):
			return self.customProperties[key]
		return False

	# Must create file structure, ask user for input, set properties, and generate a YAML!
	def create(self):
		raise NotImplementedError(type(self).__name__ + ' is required to implement create!')

	# Must confirm existence of entity via YAML, and set the directory path property!
	# Must throw an exception if not found!
	def find(self):
		raise NotImplementedError(type(self).__name__ + ' is required to implement find!')

	def update(self):
		self.updatedAt = datetime.datetime.now()
		self.refreshYAML()

	# Must DELETE the YAML file. Deleted things don't exist, but their children still do!
	def delete(self):
		self.deleteYAML()

	# Must generate the YAML structure within the entity directory
	# Can depend on the directory and file name being defined in self
	def generateYAML(self):
		raise NotImplementedError(type(self).__name__ + ' is required to implement generateYAML!')

	# Must map YAML to the entity properties
	def loadYAML(self):
		raise NotImplementedError(type(self).__name__ + ' is required to implement loadYAML!')

	def deleteYAML(self):
		yamlFilePath = self.getFullYAMLPath()

		# Check for existence...
		if (not os.path.exists(yamlFilePath)):
			raise FileExistsError("Can't delete non-existent YAML!")

		# Delete it
		os.remove(yamlFilePath)

	def refreshYAML(self):
		self.updatedAt = datetime.datetime.now()
		self.deleteYAML()
		self.generateYAML()

	# Must return path to the YAML file (relative to project base)!
	def getFullYAMLPath(self):
		return self.directory + '/' + self.name + '/' + self.entityFile

	def print(self):
		print("The Entity, %s" % self.name)
		print("----------------------------");
		print(self.description)
		print("")
		print("Created on %s" % self.createdAt.strftime("%Y-%m-%d %H:%M"))
		print("Updated on %s" % self.updatedAt.strftime("%Y-%m-%d %H:%M"))

	# Helpers mainly
	def askFor(self, prompt):
		return input(self.promptPrefix + prompt + self.promptSuffix)
