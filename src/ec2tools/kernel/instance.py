from . import misc, objects, volume
from .vars import factory

def enrich (o):
	if not o:
		o = None
	name = objects.getName(o)
	o.__setattr__('name', name)
	status = objects.getStatus(o)
	o.__setattr__('status', status)
	getRootVolume = lambda: _getRootVolume(o)
	o.__setattr__('getRootVolume', getRootVolume)
	getRootDevice = lambda: _getRootDevice(o)
	o.__setattr__('getRootDevice', getRootDevice)
	return o


def all ():
	data = [enrich(o) for o in factory.instances.all()]
	return data 


def get (id):
    o = factory.Volume(id)
    o = enrich(o)
    return o


def _getObject (arg):
	if isinstance(arg, str): 
		instance = get(arg)
	else:
		instance = arg
	return instance
	

def _getRootDevice (arg):
	instance = _getObject(arg)
	resp = instance.describe_attribute(Attribute='rootDeviceName')
	value = resp['RootDeviceName']['Value']
	return value


def _getRootVolume (arg):
	instance = _getObject(arg)
	rootDevice = _getRootDevice(instance)
	volumes = instance.volumes.all()
	attachments = misc.flattenListOfLists([v.attachments for v in volumes])
	hits = [d for d in attachments if d['State'] == 'attached' and d['Device'] == rootDevice and d['InstanceId'] == instance.id]
	dVolume = misc.justOneOrNone(hits)
	if not dVolume:
		rootVolume = None
	else:
		idVolume = dVolume['VolumeId']
		rootVolume = volume.get(idVolume)
	return rootVolume

