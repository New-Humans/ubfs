#!/usr/bin/python3

from ideas.entity import Entity


def getPathFromCDS(s):
	path = ""
	for d in s:
		path += d + '/'
	return path


def getPathFromCKS(s):
	pass


contextKeyStack = ["existence"]
contextDirStack = ["existence"]

thing = Entity("generic_object", getPathFromCDS(contextDirStack))		# get the current path using the context stack
thing.create()

