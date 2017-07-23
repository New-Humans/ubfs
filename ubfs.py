#!/usr/bin/python3

from ideas.entity import Entity
from ideas.existence import Existence
from ideas.spec import Spec
from ideas.errors import EntityKeyNotFoundError, EntityIsNotAContextError, EntityAlreadyExistsError, IllogicalEntityError, InvalidSpecStringError

# MAIN COMMAND FUNCTIONS
def help(context):
	print(context.help())

def show(entity):
	print(entity.toString())

def dump(entity):
	entity.dump()

def update(entity):
	entity.update()



# Main loop definition
def mainLoop(config, cs):
	inString = input(config['prompt'])    # The in-string! a genius name!

	# Parse the inString
	args = inString.split()

	# Main ditch out for leaving! Probably good practice
	if (args[0] == "exit"):
		return False

	# Main command structure
	frameOfReference = cs.pop()       # Use the top of the context stack as the frame of ref
	
	# HELP
	if (args[0] == "help"):
		help(frameOfReference)

	# SHOW
	elif (args[0] == "show"):
		if (len(args) < 2):
			show(frameOfReference)
		else:
			try:
				entity = frameOfReference.find(args[1])
				show(entity)
				entity = None # Good memory management? Unnecessary? You decide!
			except FileNotFoundError:
				print("There's no entity in this context with that key!")

	# USE
	elif (args[0] == "use"):
		if (len(args) < 2):
			print("Please enter a context key to use!")
		else:
			try:
				context = frameOfReference.find(args[1], True)
				cs.append(frameOfReference)
				frameOfReference = context
				context = None
			except FileNotFoundError:
				print("There's no entity in this context with that key!")
			except EntityIsNotAContextError:
				print("You can't use that entity as a frame of reference!")

	# BACK
	elif (args[0] == "back"):
		if (len(cs) < 1): # It's impossible to move outside a frame of reference
			print("You can't escape existence!")
		else:
			frameOfReference = cs.pop()

	# ADD
	elif (args[0] == "add"):
		if (len(args) < 3):
			print("Not enough arguments! Read the manual ('help')!")
		else:
			try:
				spec = Spec.getSpecFromString(args[1])
				frameOfReference.add(args[2], spec)
			except InvalidSpecStringError:
				print("That entity type can't be recognized!")
			except FileExistsError:
				print("An entity by that key already exists!")
			except IllogicalEntityError:
				print("That entity can't be created from this frame of reference!")

	# DUMP
	elif (args[0] == "dump"):
		if (len(args) < 2):
			dump(frameOfReference)
		else:
			try:
				entity = frameOfReference.find(args[1])
				dump(entity)
				entity = None # Good memory management? Unnecessary? You decide!
			except FileNotFoundError:
				print("There's no entity in this context with that key!")

	# UPDATE
	elif (args[0] == "update"):
		if (len(args) < 2):
			update(frameOfReference)
		else:
			try:
				entity = frameOfReference.find(args[1])
				update(entity)
				entity = None
			except FileNotFoundError:
				print("There's no entity in this context with that key!")

	# UNRECOGNIZED
	else:
		print("That command can't be recognized!")


	# Finish up
	cs.append(frameOfReference)
	frameOfReference = None
	return True






# NEAT COMMANDS

# Ask for definitions
def askForString(s):
	return input(s)





# Jerad's handy configuration for the main loop
config = {'prompt': '> '}




# Initialize
print("Initializing Context Stack...")
contextStack = []
print("Loading Existence...")
context = Existence('existence', '')
context.load()
print("Adjusting Frame of Reference...")
contextStack.append(context)
print("Done!")



# Main loop implementation (or wtv) (https://stackoverflow.com/a/1662176)
while (True):
	# The mainLoop has access to the context stack
	repeat = mainLoop(config, contextStack)
	if (not repeat):
		break



print("Thank you for using the Universe Builder File System!")



