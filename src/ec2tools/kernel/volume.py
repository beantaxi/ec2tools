from . import objects
from .vars import factory


###############################################################################
#
# enrich, all, get, getObject
#
###############################################################################


def enrich (o):
	if not o:
		o = None
	objects.addNameProperty(o)
	return o


def all ():
	data = [enrich(o) for o in factory.volumes.all()]
	return data 


def get (id):
    o = factory.Volume(id)
    o = enrich(o)
    return o


def getObject (arg):
	if isinstance(arg, str): 
		instance = get(arg)
	else:
		instance = arg
	return instance
