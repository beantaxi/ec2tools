import boto3
from . import AvailabilityZone, misc, objects, Subnet, volume
from .vars import factory
from ec2tools import getA


###############################################################################
#
# enrich, all, get, getObject
#
###############################################################################

def enrich (o):
	if not o:
		o = None
	objects.addNameProperty(o)
	misc.addProperty(o, 'status', _getStatus)
	misc.addMethod(o, 'attachVolumes', _attachVolumes)
	misc.addProperty(o, 'availabilityZone', _getAvailabilityZone)
	misc.addProperty(o, 'devices', _getDevices)
	misc.addProperty(o, 'rootDevice', _getRootDevice)
	misc.addProperty(o, 'rootVolume', _getRootVolume)
	return o


def all ():
	data = [enrich(o) for o in factory.instances.all()]
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




###############################################################################
#
# Functions
#
###############################################################################


def genDevices (initDevice='/dev/xvdf'):
	currDevice = initDevice
	while True:
		yield currDevice
		currDevice = getNextDevice(currDevice)


def getNextDevice (currDevice):
	nextDevice = currDevice[:-1] + chr(ord(currDevice[-1])+1)
	return nextDevice


def _getStatus (o):
	status = o.state['Name']
	return status



###############################################################################
#
# 'Methods'
#
###############################################################################


def _attachVolumes (this, volumes, initDevice=None):
	if isthis(this, str): this = getA.Instance(this)
	devices = getDevices(this)
	g = genDevices(initDevice)
	for volume in volumes:
		device = next(g)
		print("Attaching {} to {}... ".format(volume.id, device))
		this.attach_volume(VolumeId=volume.id, Device=device)


def _getAvailabilityZone (this):
	subnet = Subnet.get(this.subnet_id)
	availabilityZone = AvailabilityZone.get(subnet.availability_zone)
	return availabilityZone


def _getDevices (this):
	volumes = this.volumes.all()
	listOfLists = [o.attachments for o in volumes]
	attachments = misc.flattenListOfLists(listOfLists)
	devices = [d['Device'] for d in attachments]
	return devices


def _getRootDevice (this):
	resp = this.describe_attribute(Attribute='rootDeviceName')
	value = resp['RootDeviceName']['Value']
	return value


def _getRootVolume (this):
	rootDevice = _getRootDevice(this)
	volumes = this.volumes.all()
	attachments = misc.flattenListOfLists([v.attachments for v in volumes])
	hits = [d for d in attachments if d['State'] == 'attached' and d['Device'] == rootDevice and d['InstanceId'] == this.id]
	dVolume = misc.justOneOrNone(hits)
	if not dVolume:
		rootVolume = None
	else:
		idVolume = dVolume['VolumeId']
		rootVolume = volume.get(idVolume)
	return rootVolume
