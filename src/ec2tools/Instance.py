from ec2tools import kernel, getA, waitFor

def attachVolumes (instance, volumes, initDevice=None):
	if isinstance(instance, str): instance = getA.Instance(instance)
	devices = getDevices(instance)
	g = genDevices(initDevice)
	for volume in volumes:
		device = next(g)
		print("Attaching {} to {}... ".format(volume.id, device))
		instance.attach_volume(VolumeId=volume.id, Device=device)


def create (*, name, keyName, imageId, instanceType, securityGroup):
	instance = createAndRun(name=name, keyName=keyName, imageId=imageId, instanceType=instanceType, securityGroup=securityGroup)
	print("Waiting for instance.running... ")
	waitFor.InstanceRunning(instance.id)
	instance.stop()
	print("Waiting for instance.stopped... ")
	waitFor.InstanceStopped(instance.id)
	return instance


def createAndRun (*, name, keyName, imageId, instanceType, securityGroup):
	instances = kernel.factory.create_instances(ImageId=imageId, 
 	                                             MinCount=1, MaxCount=1,
 	                                             KeyName=keyName,
 	                                             SecurityGroups=[securityGroup],
 	                                             InstanceType=instanceType)
	instance = kernel.justOne(instances)
	kernel.setName(instance, name)
	return instance


def genDevices (initDevice='/dev/xvdf'):
	currDevice = initDevice
	while True:
		yield currDevice
		currDevice = getNextDevice(currDevice)


def getAvailabilityZone (instance):
	if isinstance(instance, str): instance = getA.Instance(instance)
	subnet = getA.Subnet(instance.subnet_id)
	availabilityZone = getA.AvailabilityZone(subnet.availability_zone)
	return availabilityZone


def getDevices (instance):
	if isinstance(instance, str): instance = getA.Instance(instance)
	volumes = instance.volumes.all()
	listOfLists = [o.attachments for o in volumes]
	attachments = kernel.flattenListOfLists(listOfLists)
	devices = [d['Device'] for d in attachments]
	return devices


def getNextDevice (currDevice):
	nextDevice = currDevice[:-1] + chr(ord(currDevice[-1])+1)
	return nextDevice
