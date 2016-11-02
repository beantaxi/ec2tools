from . import objects
from .vars import factory

def enrich (o):
	if not o:
		o = None
	name = objects.getName(o)
	o.__setattr__('name', name)
	return o


def all ():
	data = [enrich(o) for o in factory.volumes.all()]
	return data 


def get (id):
    o = factory.Volume(id)
    o = enrich(o)
    return o
