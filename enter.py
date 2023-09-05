import json
import os
import dndice
from classes.colors import Colors
from classes.entity import Entity
from classes.entity import EntityNotFoundError
from classes.entity import EntityAlreadyExistsError
from classes.context import Context
from classes.context import ContextEntityConflictError
from classes.custom.place.multiverse import Multiverse
from classes.spec import Spec
from classes.spec import InvalidSpecStringError

# Config
basePath = "reality/"
multiverseKey = "existence"
terminalHeight = 80 # 80 is full screen
historyFile = "history.json";

# Functions for this wrapper...
def nth_repl_all(s, sub, repl, nth):
	find = s.find(sub)
	# loop util we find no match
	i = 1
	while find != -1:
		# if i  is equal to nth we found nth matches so replace
		if i == nth:
			s = s[:find]+repl+s[find + len(sub):]
			i = 0
		# find + len(sub) + 1 means we start after the last match
		find = s.find(sub, find + len(sub) + 1)
		i += 1
	return s

def myPrint(txt):
	print(txt)

def myPrompt(txt):
	return input(txt)

def stringToSpec(s):
	return Spec.getSpecFromString(s)

def specToString(s):
	return Spec.getStringFromSpec(s)

def getSpacer():
	return "\n--\n"

def clearScreen():
	for i in range (0, terminalHeight):
		myPrint("")

def printActionText(str):
	for i in range (0, 2):
		myPrint("")
	myPrint(Colors.HEADER+"###### ## #  "+str+"  # # #################### #### ### ## #  #"+Colors.ENDC)

def show(entity):
	clearScreen()
	printActionText(entity.name+" ("+entity.key+")"+" <"+entity.spec.name.upper()+">")
	printContextStack()
	myPrint("")
	myPrint(entity.toString())
	# spacer = getSpacer()
	# myPrint(spacer)
	

def printContextStack():
	s = ""
	first = True
	for context in reversed(contextStack):
		if (not first):
			s += "  <-  "
		s += Colors.OKCYAN+(context.name or "Unnamed")+Colors.ENDC+Colors.OKGREEN+" <"+context.spec.name.upper()+">"+Colors.ENDC
		first = False
	myPrint(s)

def update(entity):
	entity.update()

def saveHistory(historyList):
	with open(historyFile, 'w') as file:
		file.write(json.dumps(historyList))

def coalesce(*arg):
	return reduce(lambda x, y: x if x is not None else y, arg)

def codex(filename):
	filename = filename.lower()
	for root, dirs, files in os.walk('codex'):
		for file in files:
			if file == (filename+'.md'):
				f = open(root+"\\"+file)
				codexEntryText = f.read()
				f.close()
				codexEntryText = nth_repl_all(codexEntryText, "**", Colors.ENDC, 2)
				codexEntryText = nth_repl_all(codexEntryText, "**", Colors.BOLD, 1)
				codexEntryText = nth_repl_all(codexEntryText, "##", Colors.ENDC, 2)
				codexEntryText = nth_repl_all(codexEntryText, "##", Colors.WARNING, 1)
				clearScreen()
				myPrint(Colors.HEADER+"######## ### ## #  "+file.split('.')[0].upper()+"  # ## ### ####### ## #  #"+Colors.ENDC)
				myPrint("")
				myPrint(codexEntryText)
				myPrint("")
				return
	raise CodexEntryNotFoundError

def listCodex():
	myPrint("Usage: codex [filename]. You can view the following entries:")
	first = True
	for root, dirs, files in os.walk('codex'):
		if first:
			first = False
			continue
		myPrint("Category: "+root.split('\\')[1].upper())
		for file in files:
			myPrint(" * " + file.split('.')[0].upper())


# Errors for this wrapper...
class EntityIsNotAContextError(Exception):
	pass

class CodexEntryNotFoundError(Exception):
	pass

# Create the context stack, for browsing reality
contextStack = []

# Attempt to load the root of reality... (multiverse)
clearScreen()
try:
	myPrint(Colors.WARNING+"Attempting to load a multiverse with key ("+multiverseKey+") from directory '"+basePath+"'..."+Colors.ENDC)
	existence = Multiverse(multiverseKey, basePath)
	existence.load()
	myPrint(Colors.OKGREEN+"Success!"+Colors.ENDC)
except EntityNotFoundError:
# If it doesn't exist, create it...
	myPrint(Colors.FAIL+"Nothing exists! Creating a multiverse..."+Colors.ENDC)
	existence.create()
	myPrint(Colors.OKGREEN+"Success!"+Colors.ENDC)
myPrint(Colors.UNDERLINE+"Type \"help\" for options!"+Colors.ENDC)

# Place the multiverse onto the context stack
contextStack.append(existence)

# if there is a history list, load it all
if os.path.isfile(historyFile):
	f = open(historyFile, "r")
	# print(f.read())
	historyList = json.loads(f.read())
	f.close()
	historyList.pop() # remove existence. we know its on top from above.
	historyList.reverse()
	for historyKey in historyList:
		contextStack.append(contextStack[-1].find(historyKey))
	frameOfReference = contextStack.pop()
	show(frameOfReference)
	contextStack.append(frameOfReference)




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
	argument = myPrompt((Colors.OKGREEN+"(%s)"+Colors.ENDC+"> ") % (frameOfReference.getKey()))
	# argument = myPrompt("> ")
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
	if (args[0] in ["add", "new"]):
		if (len(args) > 2):
			try:
				entitySpec = stringToSpec(args[1].lower())
				frameOfReference.add(args[2], entitySpec)
				show(frameOfReference)
				myPrint("Successfully added %s." % (args[1].lower()))
			except InvalidSpecStringError:
				myPrint("Entity type '%s' is unrecognized." % (args[1].lower()))
			except ContextEntityConflictError:
				myPrint("Entity type '%s' is unrecognized by the frame of reference." % entitySpec.name)
			except EntityAlreadyExistsError:
				myPrint("An entity with key '%s' already exists." % (args[2]))
		else:
			myPrint("Usage: add [entity] [key]. Keys are unique. The following entities are permitted here:")
			for someSpec in frameOfReference.allowedChildEntities:
				myPrint("* " + someSpec.name)

	# 0:update 1:key
	elif (args[0] in ["update", "edit"]):
		if (len(args) > 1):
			try:
				entity = frameOfReference.find(args[1])
				update(entity)
				show(frameOfReference)
			except EntityNotFoundError:
				myPrint("No entity with the key '%s' exists in this frame of reference." % (args[1]))
		else:
			update(frameOfReference)
			
	# 0:show 1:key
	elif (args[0] in ["show", "ls"]):
		if (len(args) > 1):
			if args[1] == "..":
				if (len(contextStack) >= 1):
					show(contextStack[-1])
				else:
					myPrint("Cannot show outside the multiverse.")
			else:
				try:
					show(frameOfReference.find(args[1]))
				except EntityNotFoundError:
					myPrint("No entity with the key '%s' exists in this frame of reference." % (args[1]))
		else:
			show(frameOfReference)

	# 0:delete 1:key
	elif (args[0] == "delete"):
		myPrint("Delete stub!")

	# 0:use 1:key
	elif (args[0] in ["use", "cd"]):
		if (len(args) > 1):
			if args[1] == "..": # copy paste from back: logic
				if (len(contextStack) >= 1):
					frameOfReference = contextStack.pop()
					show(frameOfReference)
				else:
					myPrint("Cannot move outside the multiverse.")
			else:
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

	# 0:show 1:file
	elif (args[0] in ["codex", "x"]):
		if (len(args) > 1):
			try:
				codex(args[1])
			except CodexEntryNotFoundError:
				myPrint("No codex entry with the file name '%s' exists." % (args[1]))
		else:
			listCodex()

	elif (args[0] in ["r", "roll"]):
		if (len(args) > 1):
			if args[1].startswith('d'):
				result = dndice.verbose('1'+args[1])
			else:
				result = dndice.verbose(args[1])
			myPrint(result)
		else:
			myPrint("Usage: roll [#d#+#]")


	# 0:back
	elif (args[0] == "back"):
		if (len(contextStack) >= 1):
			frameOfReference = contextStack.pop()
			show(frameOfReference)
		else:
			myPrint("Cannot move outside the multiverse.") 

	# 0:help
	elif (args[0] == "help"):
		myPrint("Commands: ")
		myPrint("  add    [entity] [key] Add a new entity to the current frame of reference")
		myPrint("  update [?key]         Key optional. Update the entity")
		myPrint("  ls     [?key]         Key optional. Show the entity")
		myPrint("  delete [?key]         Key optional. Delete the entity")
		myPrint("  cd     [key]          Attempt to use the given entity as the current frame of reference")
		myPrint("  codex  [file]         Read a codex entry.")
		myPrint("  roll   [#d#+#]        Roll some dice")
		myPrint("  back                  Move back a context on the stack")
		myPrint("  exit                  Save and quit.")

	# 0:exit
	elif (args[0] == "exit"):
		myPrint("Exiting...")
		keyHistory = [frameOfReference.key]
		while contextStack:
			keyHistory.append(contextStack.pop().key)
		saveHistory(keyHistory);

	# 0:???
	else:
		myPrint("Operation not recognized. Try 'help'")

	# Re-append the current frameOfReference
	contextStack.append(frameOfReference)

