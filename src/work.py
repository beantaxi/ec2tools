import sys
import ec2tools;
from ec2tools import allThe, api, findA, getA, listThe, waitFor, Constants, _kernel as k; 
from ec2tools import Instance, Snapshot
from pprint import pprint


def createInstance ():
	imageId = Constants.AMI_Ubuntu
	keyName = 'igor'
	securityGroup = 'setup'
	# name = 'test'
	name = 'buster'
	# instanceType = 't2.micro'
	instanceType = 'i2.2xlarge'
	instance = Instance.create(name=name, imageId=imageId, instanceType=instanceType, securityGroup=securityGroup, keyName=keyName)	
	return instance


def createVolumes (wait=True):
	snapshotIds = testArgs.get('snapshotIds', [testArgs['idSnapshot']])
	instance = getTestInstance()
	az = Instance.getAvailabilityZone(instance)
	volumeType = testArgs['volumeType']
	volumes = [Snapshot.createVolume(id, az.name, volumeType=volumeType) for id in snapshotIds]
	if wait:
		volumeIds = [o.id for o in volumes]
		waitFor.VolumeAvailable(volumeIds)
	return volumes


def getTestInstance ():
	name = testArgs['instanceName']
	instance = findA.Instance(name=name)
	return instance

setupUseMe2 ():
	instance = getTestInstance()
	az = Instance.getAvailabilityZone(instance)
	#	volume = 


testArgs = {
	'instanceName': 'igor',
#	'snapshotIds': ['snap-ec2848af', 'snap-e209eebd', 'snap-031d4754', 'snap-343ba410', 'snap-95eba9a6'],
	'idSnapshot': 'snap-ec2848af',
	'volumeType': 'gp2'
}

if __name__ == '__main__':
	print('Getting instance... ')
	instance = getTestInstance()
	print('Creating volumes from snapshots... ')
	volumes = createVolumes()
	print('Attaching volumes to {}... '.format(instance.name))
	Instance.attachVolumes(instance, volumes)
