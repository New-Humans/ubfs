from ..entity import Entity
import yaml
import datetime
import os

class Universe(Entity):
	"""The top level location class"""

	# Properties (plus inherited)
	galaxies = []
	directory = 'universes'

	# Actions (plus inherited)
	def __init__(self, name):
		super().__init__(name)

	def create(self):
		# Let's bug the user for some info
		newFriendly = self.askFor("Hi! What do you want your universe to be called?")
		newDescription = self.askFor("What the heck's going on in there?")

		# Set the new info
		self.setFriendly(newFriendly)
		self.setDescription(newDescription)
		self.createdAt = datetime.datetime.now()
		self.updatedAt = datetime.datetime.now()

		# Zero'th things zero-th
		newUniPath = self.directory + '/' + self.name

		# Check for existence...
		if (os.path.exists(newUniPath)):
			raise FileExistsError("This universe already exists!")

		# Make it...
		os.makedirs(newUniPath)

		# First thing's first
		self.generateYAML()

		# Then the galaxies directory
		galaxiesDir = self.directory + '/' + self.name + '/galaxies'
		os.makedirs(galaxiesDir)

	def find(self, universeName):
		self.name = universeName
		if (not os.path.exists(self.getFullYAMLPath())):
			raise FileNotFoundError("This universe cannot be found!")

		# As a bonus
		self.name = universeName

	def generateYAML(self):
		# Grab the path to the YAML file
		yamlPath = self.getFullYAMLPath()

		# Check for existence...
		if (os.path.exists(yamlPath)):
			raise FileExistsError("This universe YAML already exists!")

		# Create the file stream, serialize the universe into YAML, and save it
		stream = open(yamlPath, 'w')
		universe = {
			"name": self.name,
			"friendly": self.friendly,
			"description": self.description,
			"createdAt": self.createdAt.strftime("%Y-%m-%d %H:%M:%S.%f"),
			"updatedAt": self.updatedAt.strftime("%Y-%m-%d %H:%M:%S.%f")
		}
		yaml.dump(universe, stream)
		stream.close()
	
	def loadYAML(self):
		stream = open(self.directory + '/' + self.name + '/' + self.entityFile, 'r')

		universe = yaml.load(stream)
		stream.close()

		self.name = universe['name']
		self.friendly = universe['friendly']
		self.description = universe['description']
		self.createdAt = datetime.datetime.strptime(universe['createdAt'], "%Y-%m-%d %H:%M:%S.%f")
		self.updatedAt = datetime.datetime.strptime(universe['updatedAt'], "%Y-%m-%d %H:%M:%S.%f")

	def print(self):
		print("The universe '%s'" % self.friendly)
		print("----------------------------");
		print(self.description)
		print("")
		print("Created on %s" % self.createdAt.strftime("%Y-%m-%d %H:%M"))
		print("Updated on %s" % self.updatedAt.strftime("%Y-%m-%d %H:%M"))
