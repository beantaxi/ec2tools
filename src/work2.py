import ec2tools;
from ec2tools import allThe, api, findA, getA, listThe, waitFor, Constants, _kernel as k; 
from ec2tools import Instance, Snapshot
from pprint import pprint

def createInstance ():
	imageId = Constants.AMI_Ubuntu
	keyName = 'igor'
	securityGroup = 'setup'
	name = 'test'
	# name = 'buster'
	instanceType = 't2.micro'
	# instanceType = 'i2.2xlarge'
	instance = Instance.create(name=name, imageId=imageId, instanceType=instanceType, securityGroup=securityGroup, keyName=keyName)	


if __name__ == '__main__':
	volumeIds = []

	createInstance()
# 	idSnapshot='snap-95eba9a6'
# 	snapshotIds = ['snap-ec2848af', 'snap-e209eebd', 'snap-031d4754', 'snap-343ba410', 'snap-95eba9a6']
# 	instance = findA.Instance(name='igor')
# 	az = Instance.getAvailabilityZone(instance)
# 	pprint(az)
# 	volumes = [Snapshot.createVolume(id, az.name) for id in snapshotIds]
# 	volumeIds = [o.id for o in volumes]
# 	print("Waiting for volumes to be available... ")
# 	waitFor.VolumeAvailable(volumeIds)
# 	Instance.attachVolumes(instance, volumes)
	
