import datetime
from ...thing import Thing
from ...spec import Spec

class ShoppingList(Thing):
	"""Books can have pages! Found in many places.

	Attributes
		Nothing much yet!"""

	# Things that child class SHOULDNT need to redeclare
	items = []
	
	# Things that a few child classes will need to redeclare

	# Things every child class will want to redeclare
	spec = Spec.SHOPPINGLIST

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
		while (choice != 5):
			choice = None 	
			while (choice != 1 and choice != 2 and choice != 3 and choice != 4 and choice != 5):
				print("Please select an action")
				print("  1) Edit name")
				print("  2) Edit description")
				print("  3) Add item")
				print("  4) Remove item")
				print("  5) save and continue navigating")
				choice = self.askForInteger("Action")

				if (choice != 1 and choice != 2 and choice != 3 and choice != 4 and choice != 5):
					print("Invalid choice!")

			if (choice == 1):
				self.setName(self.askForString("You erase the list's title and write"))
			elif (choice == 2):
				self.setDescription(self.askForString("You update the list's description to read"))
			elif (choice == 3):
				self.addItem(self.askForString("Add to list"))
			elif (choice == 4):
				print(self.getAllItemsStr())
				removeIndex = self.askForInteger("Remove entry")
				print("Removing %s..." % (self.items[removeIndex - 1]))
				self.removeItem(removeIndex - 1)
			elif (choice == 5):
				print("Saving %s..." % self.getSpecString())
				self.setUpdatedAt(datetime.datetime.now())
				self.refreshYAML()
				print("Saved!")

	def toString(self):
		"""Represent the entity attributes as a string.

		Will redefine on many entities

		Arguments
		None

		Return
		string"""
		s = "A %s titled '%s':\n\n" % (self.getSpecString(), self.getName())
		s += "It's summary reads: %s\n\n" % (self.getDescription())
		s += "~~\n%s\n~~" % (self.getAllItemsStr())
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
			"items": self.getAllItems()
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
		self.setAllItems(entityDict['items'])

	# Getters / Setters
	def getAllItems(self):
		return self.items

	def setAllItems(self, items):
		self.items = items

	def removeItem(self, index):
		self.items.pop(index)

	def addItem(self, itemStr):
		self.items.append(itemStr)

	def getAllItemsStr(self):
		c = 1
		s = ""
		for i in self.items:
			d = str(c) + "."
			s += "  %4s  %s\n" % (d, i)
			c = c + 1
		return s

	