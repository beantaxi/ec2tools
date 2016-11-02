from . import objects

def enrichSnapshot (o):
	if not o:
		o = None
	name = objects.getName(o)
	o.__setattr__('name', name)
	return o



