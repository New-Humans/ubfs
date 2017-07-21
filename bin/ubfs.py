#!/usr/bin/python3

from classes.entity import Entity
from classes.locations.universe import Universe

import sys

## HELPERS ##
def checkAllowed(needle, haystack):
	# The haystack is a list of allowed commands. The needle must be among them
	if (needle in haystack):
		return True
	else:
		return False



## EXECUTION ##

# Collect arguments (ditch file path) + validations(?)
args = sys.argv[1:]

# ARGUMENT 1 - The action
action = args[0]
if (not checkAllowed(action, ["add", "edit", "show", "delete"])):
	print("The action '%s' is not allowed! (argument 1)" % action)
	sys.exit(1)

if (action == "add"):
	# ARGUMENT 2 - The context
	context = args[1]
	if (not checkAllowed(context, ["universe"])):
		print("The context '%s' is not allowed! (argument 2)" % context)
		sys.exit(1)

	if (context == "universe"):
		# ARGUMENT 3 - The name of the universe
		universeName = args[2]

		universe = Universe(universeName)
		universe.create()
		print()
		universe.print()

elif (action == "edit"):
	# ARGUMENT 2 - The context
	context = args[1]
	if (not checkAllowed(context, ["universe"])):
		print("The context '%s' is not allowed! (argument 2)" % context)
		sys.exit(1)

	# ARGUMENT 3 - The context name
	contextName = args[2]

	if (context == "universe"):
		entity = Universe(None)

	entity.find(contextName)
	entity.loadYAML()
	# ARGUMENT 4 - The property to edit
	prop = args[3]
	if (not checkAllowed(prop, ["friendly", "description"])):
		print("The property '%s' is not allowed! (argument 4)" % prop)
		sys.exit(1)

	# ARGUMENT 5 - the value to assign it
	value = args[4]

	if (prop == "friendly"):
		entity.setFriendly(value)
	elif (prop == "description"):
		entity.setDescription(value)

	entity.update()

elif (action == "show"):
	# ARGUMENT 2 - The context
	context = args[1]
	# ARGUMENT 3 - The context name
	contextName = args[2]

	if (context == "universe"):
		entity = Universe(None)

	entity.find(contextName)
	entity.loadYAML()

	print()
	entity.print()

elif (action == "delete"):
	# ARGUMENT 2 - The context
	context = args[1]
	# ARGUMENT 3 - The context name
	contextName = args[2]

	if (context == "universe"):
		entity = Universe(None)

	entity.find(contextName)
	entity.delete()

	print()
	print("The %s '%s' was deleted." % context, contextName)
