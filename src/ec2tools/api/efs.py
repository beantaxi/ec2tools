from ec2tools import *
from ec2tools import kernel

def createFileSystem (name=None):
	idFileSystem = Efs.createFileSystem(name)
	while Efs.client.describe_file_systems(FileSystemId=idFileSystem)['FileSystems'][0]['LifeCycleState'] == 'creating':
		pass
	print('idFileSystem='+idFileSystem)
	subnets = _getOneSubnetPerAz()
	for subnet in subnets:
		print("idFileSystem={} subnet.id={}".format(idFileSystem, subnet.id))
		Efs.createMountTarget(idFileSystem, subnet.id)
	return idFileSystem


def deleteFileSystem (id):
	resp = Efs.client.describe_mount_targets(FileSystemId=id)
	mountTargets = resp['MountTargets']
	mountTargetIds = [d['MountTargetId'] for d in mountTargets]
	for idMountTarget in mountTargetIds:
		Efs.client.delete_mount_target(MountTargetId=idMountTarget)
	Efs.client.delete_file_system(FileSystemId=id)


def _getOneSubnetPerAz ():
	allAzs = allThe.AvailabilityZones()
	allSubnets = allThe.Subnets()
	subnets = [_getSubnetForAz(o, allSubnets) for o in allAzs]
	return subnets


def _getSubnetForAz (az, subnets):
	hits = [o for o in subnets if o.availability_zone == az.name]
	if not hits:
		raise Exception("No subnet for {}".format(az.name))
	subnet = hits[0]
	return subnet


def getMountTargetForInstance (fileSystem, instance):
	mountTargets = Efs.getMountTargets(fileSystem)
	fn = lambda o: _isMountTargetForInstance(o, instance)
	mountTarget = kernel.first(mountTargets, fn)
	return mountTarget


def getMountUrl (fileSystem, instance):
	mountTarget = getMountTargetForInstance(fileSystem, instance)
	subnet = getA.Subnet(mountTarget.idSubnet)
	az = getA.AvailabilityZone(subnet.availability_zone)
	mountUrl = "{}.{}.efs.{}.amazonaws.com".format(az.name, mountTarget.idFileSystem, az.region)
	return mountUrl


def _isMountTargetForInstance (mountTarget, instance):
	azMountTarget = getA.Subnet(mountTarget.idSubnet).availability_zone
	azInstance = getA.Subnet(instance.subnet_id).availability_zone
	flag = azMountTarget == azInstance
	return flag
