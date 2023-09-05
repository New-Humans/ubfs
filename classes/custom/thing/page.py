import datetime
from ...thing import Thing
from ...spec import Spec

class Page(Thing):
	"""A page! Kind of like a document. Found in books, loose, in folders, etc

	Attributes
		Content!!"""

	# Things that child class SHOULDNT need to redeclare
	content = None

	# Things that a few child classes will need to redeclare

	# Things every child class will want to redeclare
	spec = Spec.PAGE

	# ---- Methods ---- #
	def update(self):
		"""Display and handle interaction for a menu that updates this entity's properties.
		
		Should and will want to redefine.

		Arguments
		None

		Return
		None"""
		print("Editing %s '%s'" % (self.getSpecString(), self.getName()))
		choice = None
		while (choice != 4):
			choice = None 	
			while (choice != 1 and choice != 2 and choice != 3 and choice != 4):
				print("Please select an action")
				print("  1) Edit title")
				print("  2) Edit summary")
				print("  3) Edit content")
				print("  4) save and continue navigating")
				choice = self.askForInteger("Action")

				if (choice != 1 and choice != 2 and choice != 3 and choice != 4):
					print("Invalid choice!")

			if (choice == 1):
				self.setName(self.askForString("You erase the %s's title and write" % self.getSpecString()))
			elif (choice == 2):
				self.setDescription(self.askForString("You update tha %s's summary to read" % self.getSpecString()))
			elif (choice == 3):
				self.setContent(self.askForDocument("You update the %s content, using document notation" % self.getSpecString()))
			elif (choice == 4):
				self.setUpdatedAt(datetime.datetime.now())
				self.refreshYAML()
				print("You finish updating the page.")

	def toString(self):
		"""Represent the entity attributes as a string.

		Will redefine on many entities

		Arguments
		None

		Return
		string"""
		s = "A %s titled '%s':\n\n" % (self.getSpecString(), self.getName())
		s += "It's summary reads: %s\n\n" % (self.getDescription())
		s += "~~\n%s\n~~" % (self.getContent())
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
			"content": self.getContent()
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
		self.setContent(entityDict['content'])


	# Getters / Setters
	def getContent(self):
		return self.content

	def setContent(self, c):
		self.content = c
