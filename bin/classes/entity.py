import yaml
import datetime

# Entity class for Universe builder
# EVERYTHING is an entity! Maybe (probably)!
class Entity:
	"""Encompessing parent class for all other UBFS objects"""

	# Properties
	name = None
	description = None
	createdAt = None
	updatedAt = None
	customProperties = {}

	# Actions
	def __init__(self, name):
		self.name = name
		self.createdAt = datetime.datetime.now()
		self.updatedAt = datetime.datetime.now()

	def setName(self, name):
		self.name = name
		self.save()

	def setDescription(self, description):
		self.description = description
		self.save()

	def setCustomProperty(self, key, value):
		self.customProperties[key] = value;

	def getCustomProperty(self, key):
		if (key in self.customProperties)
			return self.customProperties[key]
		return false

	def create(self):
		raise NotImplementedError(type(self).__name__ + ' is required to implement create!')

	def save(self):
		self.updatedAt = datetime.datetime.now()
		self.deleteYAML()
		self.generateYAML()

	def generateYAML(self):
		raise NotImplementedError(type(self).__name__ + ' is required to implement generateYAML!')

	def loadYAML(self):
		raise NotImplementedError(type(self).__name__ + ' is required to implement loadYAML!')

	def deleteYAML(self):
		raise NotImplementedError(type(self).__name__ + ' is required to implement deleteYAML!')

	def print(self):
		print("The Entity, " + self.name)
		print("----------------------------");
		print(self.description)
		print("")
		print("Created on %s" % self.createdAt.strftime("%Y-%m-%d %H:%M"))
		print("Updated on %s" % self.updatedAt.strftime("%Y-%m-%d %H:%M"))
