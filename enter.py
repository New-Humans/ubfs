from classes.entity import Entity
from classes.entity import EntityNotFoundError
from classes.entity import EntityAlreadyExistsError
from classes.context import Context
from classes.context import ContextEntityConflictError
from classes.custom.place.universe import Universe
from classes.spec import Spec
from classes.spec import InvalidSpecStringError

# Config
basePath = "reality/"
universeKey = "existence"
terminalHeight = 80

# Functions for this wrapper...
def myPrint(txt):
	print(txt)

def myPrompt(txt):
	return input(txt)

def stringToSpec(s):
	return Spec.getSpecFromString(s)

def getSpacer():
	return "\n--\n"

def clearScreen():
	for i in range (0, terminalHeight):
		myPrint("")

def show(entity):
	clearScreen()
	spacer = getSpacer()
	myPrint(spacer)
	myPrint(entity.toString())
	myPrint("")

def update(entity):
	entity.update()
	show(entity)

# Errors for this wrapper...
class EntityIsNotAContextError(Exception):
	pass

# Attempt to load the root of reality... (universe)
try:
	myPrint("Attempting to load existence...")
	existence = Universe(universeKey, basePath)
	existence.load()
	myPrint("Done!")
	show(existence)
except EntityNotFoundError:
# If it doesn't exist, create it...
	myPrint("Nothing exists! Creating a universe...")
	existence.create()

# Create the context stack, for browsing reality
contextStack = []

# Place the universe onto the context stack
contextStack.append(existence)

# Begin main loop
# Main loop assumes that the context stack has the current context at top
# It will pull it off and perform interactions on the current context, based on user input
# Valid commands include [add [entity] [key], update [key], show [key], delete [key]], use [key]
# A user should be asked for a command each loop, and can end any time by typing 'exit'
args = [-1]
while (args[0] != "exit"):
	# Pop off the current frame of reference
	frameOfReference = contextStack.pop()

	# Get the users choice
	argument = myPrompt("%s %s> " % (frameOfReference.getSpecString(), frameOfReference.getKey()))
	if (argument == ""):  # No input condition
		# Re-append the current frameOfReference
		contextStack.append(frameOfReference)
		continue

	# Split it into an array of strings
	# 0 -> the original command [add, update, show, delete]
	# 1 -> the entity type-string if add, the entity key otherwise (key is optional. No key passed - operate on self)
	# 2 -> The entity key, if add. Not used otherwise
	args = argument.split()
	
	# Handle
	# 0:add 1:entity 2:key
	if (args[0] == "add"):
		if (len(args) > 2):
			try:
				entitySpec = stringToSpec(args[1])
				frameOfReference.add(args[2], entitySpec)
				show(frameOfReference)
				myPrint("Successfully added %s." % (args[1]))
			except InvalidSpecStringError:
				myPrint("Entity type '%s' is unrecognized." % (args[1]))
			except ContextEntityConflictError:
				myPrint("Entity type '%s' is unrecognized by the frame of reference." % entitySpec.name)
			except EntityAlreadyExistsError:
				myPrint("An entity with key '%s' already exists." % (args[2]))
		else:
			myPrint("Usage: add [entity] [key]. Keys are unique.")

	# 0:update 1:key
	elif (args[0] == "update"):
		if (len(args) > 1):
			try:
				entity = frameOfReference.find(args[1])
				update(entity)
			except EntityNotFoundError:
				myPrint("No entity with the key '%s' exists in this frame of reference." % (args[1]))
		else:
			update(frameOfReference)
			
	# 0:show 1:key
	elif (args[0] == "show"):
		if (len(args) > 1):
			try:
				entity = frameOfReference.find(args[1])
				show(entity)
			except EntityNotFoundError:
				myPrint("No entity with the key '%s' exists in this frame of reference." % (args[1]))
		else:
			show(frameOfReference)

	# 0:delete 1:key
	elif (args[0] == "delete"):
		myPrint("Delete stub!")

	# 0:use 1:key
	elif (args[0] == "use"):
		if (len(args) > 1):
			try:
				context = frameOfReference.find(args[1])
				if (not context.getIsContext()):
					raise EntityIsNotAContextError("Attempted to use entity as a context, when it is not.")
				contextStack.append(frameOfReference)
				frameOfReference = context
				show(frameOfReference)
			except EntityNotFoundError:
				myPrint("No entity with the key '%s' exists in this frame of reference." % (args[1]))
			except EntityIsNotAContextError:
				myPrint("'%s' is not a contextual entity and cannot be used." % (args[1]))
		else:
			myPrint("Usage: use [key]. Keys are unique.")

	# 0:back
	elif (args[0] == "back"):
		if (len(contextStack) >= 1):
			frameOfReference = contextStack.pop()
			show(frameOfReference)
		else:
			myPrint("Cannot move outside the universe.") 

	# 0:help
	elif (args[0] == "help"):
		myPrint("Commands: ")
		myPrint("  add    [entity] [key] Add a new entity to the current frame of reference")
		myPrint("  update [?key]         Key optional. Update the entity")
		myPrint("  show   [?key]         Key optional. Show the entity")
		myPrint("  delete [?key]         Key optional. Delete the entity")
		myPrint("  use    [key]          Attempt to use the given entity as the current frame of reference")
		myPrint("  back                  Move back a context on the stack")

	# 0:exit
	elif (args[0] == "exit"):
		myPrint("Exiting...")

	# 0:???
	else:
		myPrint("Operation not recognized. Try 'help'")

	# Re-append the current frameOfReference
	contextStack.append(frameOfReference)

