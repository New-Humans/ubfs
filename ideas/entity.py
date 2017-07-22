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

		@staticmethod
		def getSpec(self):
			return self.spec






	# Helpers mainly
	# Rescued from 1.0, I liked it so much
	def askFor(self, prompt):
		return input(self.promptPrefix + prompt + self.promptSuffix)

