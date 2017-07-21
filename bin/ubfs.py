#!/usr/bin/python3

from classes.entity import Entity
from classes.locations.universe import Universe

import sys

# Main file for interaction with a universe!! Exciting.
# Has to handle commands and using the entity classes.
# For now, it'll just be testing!

# Collect arguments (ditch file path) + validations(?)
args = sys.argv[1:]

# ARGUMENT 1 - The action
action = args[0]

if (action == "add"):
	# ARGUMENT 2 - The context
	context = args[1]

	if (context == "universe"):
		# ARGUMENT 3 - The name of the universe
		universeName = args[2]

		universe = Universe(universeName)
		universe.generateYAML()

elif (action == "edit"):
	# ARGUMENT 2 - The context
	context = args[1]
	# ARGUMENT 3 - The context name
	contextName = args[2]

	if (context == "universe"):
		entity = Universe(None)
		entity.loadYAML(contextName)

	# ARGUMENT 4 - The property to edit
	prop = args[3]

	# ARGUMENT 5 - the value to assign it
	value = args[4]

	if (prop == "name"):
		entity.setName(value)
	elif (prop == "description"):
		entity.setDescription(value)
