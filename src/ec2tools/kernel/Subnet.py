from .vars import factory

###############################################################################
#
# enrich, all, get, getObject
#
###############################################################################


def all ():
	data = factory.snapshots.all()
	return data 


def get (id):
    o = factory.Subnet(id)
    return o


def getObject (arg):
	if isinstance(arg, str): 
		instance = get(arg)
	else:
		instance = arg
	return instance





