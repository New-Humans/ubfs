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

	def create(self):
		pass

	def save(self):
		self.updatedAt = datetime.datetime.now()
		self.deleteYAML()
		self.generateYAML()

	def generateYAML(self):
		raise NotImplementedError(type(self).__name__ + ' is required to implement genYAML!')

	def loadYAML(self):
		raise NotImplementedError(type(self).__name__ + ' is required to implement loadYAML!')

	def deleteYAML(self):
		raise NotImplementedError(type(self).__name__ + ' is required to implement deleteYAML!')

	def print(self):
		print(self.name)
		print("----------------------------");
		print(self.description)
		print("")
		print("Created on %s" % self.createdAt.strftime("%Y-%m-%d %H:%M"))
		print("Updated on %s" % self.updatedAt.strftime("%Y-%m-%d %H:%M"))
