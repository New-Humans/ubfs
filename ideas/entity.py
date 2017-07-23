from .spec import Spec
import yaml
import datetime
import os

# Entity class
# Concerns itself
class Entity:
	"""Encompessing parent class for most other people, places, and things"""

	# An entity must have...
	# Saveable / editable (stored on saves and updates)
	key = None
	spec = Spec.ENTITY            # This is a reference to different types of entities
	name = None
	description = None
	createdAt = None
	updatedAt = None

	# Control - non seriazable
	path = None                   # Must end in [key]
	YAMLFileName = "entity.yaml"
	promptPrefix = "> "
	promptSuffix = ": "



	# An entity must be able to...
	def __init__(self, key, path):
		"""Every entity must be initialized with a path, and a key"""
		self.key = key
		self.path = path + key


	def create(self):
		"""Create implies we're generating a brand new entity. Not a copy of an existing one"""
		# Check the entity with the same key (directory) doesn't exist
		if (os.path.exists(self.path)):
			raise FileExistsError("This " + self.spec.name + " already exists!")

		self.name = self.askFor("Please enter a name for this entity")
		self.description = self.askFor("Please enter a description for this entity")
		self.createdAt = datetime.datetime.now()
		self.updatedAt = datetime.datetime.now()

		os.makedirs(self.path)
		self.createYAML()

		
	def createYAML(self):
		"""Assumes YAML file for the entity does not exist yet. Creates it"""
		fullPath = self.path + '/' + self.YAMLFileName
		if (os.path.exists(fullPath)):
			raise FileExistsError("This " + self.spec.name + " already exists!")

		stream = open(fullPath, 'w')
		entity = {
			"key": self.key,
			"spec": self.spec,
			"name": self.name,
			"description": self.description,
			"createdAt": self.createdAt.strftime("%Y-%m-%d %H:%M:%S.%f"),
			"updatedAt": self.updatedAt.strftime("%Y-%m-%d %H:%M:%S.%f"),
		}

		yaml.dump(entity, stream)
		stream.close()


	def load(self):
		"""Load implies we're loading an existing entity."""
		# Check the directory and file exist
		if (not os.path.exists(self.path + '/' + self.YAMLFileName)):
			raise FileNotFoundError("The " + self.spec.name + " could not be found!")

		# Load the YAML!
		self.loadYAML()


	def loadYAML(self):
		"""Assumes YAML file for the entity does exist. Loads the YAML into the object"""
		# Check the directory and file exist
		fullEntityPath = self.path + '/' + self.YAMLFileName
		if (not os.path.exists(fullEntityPath)):
			raise FileNotFoundError("The " + self.spec.name + " could not be found!")

		# The loading!
		stream = open(fullEntityPath, 'r')
		entity = yaml.load(stream)
		stream.close()

		# The referencing!
		self.spec = entity['spec']
		self.name = entity['name']
		self.description = entity['description']
		self.createdAt = datetime.datetime.strptime(entity['createdAt'], "%Y-%m-%d %H:%M:%S.%f")
		self.updatedAt = datetime.datetime.strptime(entity['updatedAt'], "%Y-%m-%d %H:%M:%S.%f")


	def toString(self):
		""" Generate and return a string representation of the entity"""
		s = ("# " + self.name + "\n"
			 "\n## Description\n"
			 "" + self.description + "\n"
			 "\n## Timestamps\n"
			 "Created at " + self.createdAt.strftime("%Y-%m-%d %H:%M") + "\n"
			 "Updated at " + self.updatedAt.strftime("%Y-%m-%d %H:%M")
			)

		return s

	def dump(self):
		"""Dump to debug info to console"""
		print("Key:  %s\nSpec: %s\nPath: %s" % (self.key, self.spec.name, self.path))

	
	def getSpec(self):
		return self.spec


	# Helpers mainly
	# Rescued from 1.0, I liked it so much
	def askFor(self, prompt):
		return input(self.promptPrefix + prompt + self.promptSuffix)

