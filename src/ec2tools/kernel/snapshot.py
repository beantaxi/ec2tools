from . import misc, objects
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
	misc.addMethod(o, 'createVolume', _createVolume) 
	return o


def all ():
	data = [enrich(o) for o in factory.snapshots.all()]
	return data 


def get (id):
    o = factory.Snapshot(id)
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
# Methods
#
###############################################################################


def _createVolume (this, availabilityZone, volumeType='gp2'):
	idSnapshot = this.id
	if volumeType == 'io1':
		iops = 30*this.volume_size    # The maximum allowable
		volume = factory.create_volume(SnapshotId=idSnapshot, AvailabilityZone=availabilityZone, VolumeType=volumeType, Iops=iops)
	else:
		print("Creating snapshot for '{}'... ".format(idSnapshot))
		volume = factory.create_volume(SnapshotId=idSnapshot, AvailabilityZone=availabilityZone, VolumeType=volumeType)
	volume.name = this.name
	return volume
