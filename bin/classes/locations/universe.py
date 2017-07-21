from ..entity import Entity
import yaml
import datetime
import os

from pprint import pprint

class Universe(Entity):
	"""The top level location classes"""

	# Properties (plus inherited)
	galaxies = []

	# Actions (plus inherited)
	def __init__(self, name):
		super().__init__(name)

	def generateYAML(self):
		# Make a directory name for the new universe, in the universes directory
		directory = 'universes/' + self.name

		# Check for existence...
		if (os.path.exists(directory)):
			raise FileExistsError("This universe already exists!")

		# Make it...
		os.makedirs(directory)

		# Create the file stream, serialize the universe into YAML, and save it
		stream = open(directory + '/entity_meta.yaml', 'w')
		universe = {
			"name": self.name,
			"description": self.description,
			"createdAt": self.createdAt.strftime("%Y-%m-%d %H:%M:%S.%f"),
			"updatedAt": self.updatedAt.strftime("%Y-%m-%d %H:%M:%S.%f")
		}
		yaml.dump(universe, stream)
		stream.close()
	
	def loadYAML(self, universeName):
		directory = 'universes/' + universeName

		if (not os.path.exists(directory)):
			raise FileNotFoundError("This universe cannot be found!")

		stream = open(directory + '/entity_meta.yaml', 'r')

		universe = yaml.load(stream)
		stream.close()

		self.name = universe['name']
		self.description = universe['description']
		self.createdAt = datetime.datetime.strptime(universe['createdAt'], "%Y-%m-%d %H:%M:%S.%f")
		self.updatedAt = datetime.datetime.strptime(universe['updatedAt'], "%Y-%m-%d %H:%M:%S.%f")
		
	def deleteYAML(self):
		yamlFile = 'universes/' + self.name + '/entity_meta.yaml'

		# Check for existence...
		if (not os.path.exists(yamlFile)):
			raise FileExistsError("Can't delete non-existant YAML!")

		# Make it...
		os.remove(yamlFile)

	def print(self):
		print("The universe of %s" % self.name)
		print("----------------------------");
		print(self.description)
		print("")
		print("Created on %s" % self.createdAt.strftime("%Y-%m-%d %H:%M"))
		print("Updated on %s" % self.updatedAt.strftime("%Y-%m-%d %H:%M"))
