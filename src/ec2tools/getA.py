from ec2tools import kernel
from ec2tools import Efs

# From http://stackoverflow.com/questions/652276/is-it-possible-to-create-anonymous-objects-in-python
class Mocker(object):
	def __init__ (self, **kwargs):
		self.__dict__.update(kwargs)


def Address (d):
	if d['Domain'] == 'classic':
		id = d['PublicIp']
		o = kernel.factory.ClassicAddress(id)
	elif d['Domain'] == 'vpc':
		id = d['AllocationId']
		o = kernel.factory.VpcAddress(id)
	else:
		raise Exception("Unknown address type: '{}'".format(d['Domain']))
	return o


class _AvailabilityZone:
	def __init__ (self, d):
		self.name = d['ZoneName']
		self.state = d['State']
		self.region = d['RegionName']
		self.messages = [m['Message'] for m in d['Messages']]


def AvailabilityZone (name):
	zoneNames = [name]
	resp = kernel.cli.describe_availability_zones(ZoneNames=zoneNames)
	rawData = resp['AvailabilityZones']
	d = kernel.justOne(rawData)
	o = _AvailabilityZone(d)
	return o


class _FileSystem:
	def __init__ (self, d):
		self.name = d['Name']
		self.ownerId = d['OwnerId']
		self.id = d['FileSystemId']
		self.creationTime = d['CreationTime']
		self.size = d['SizeInBytes']['Value']
		self.sizeTimestamp = d['SizeInBytes'].get('Timestamp', 0)
		self.state = d['LifeCycleState']
		self.mountTargetCount = d['NumberOfMountTargets']
		self.mode = d['PerformanceMode']


def FileSystem (id):
	resp = Efs.client.describe_file_systems(FileSystemId=id)
	hits = resp.get('FileSystems', None)
	hit = kernel.justOne(hits)
	o = _FileSystem(hit)
	return o


def Instance (id):
    o = kernel.instance.get(id)
    return o


def InternetGateway (id):
    o = kernel.factory.InternetGateway(id)
    return o

def KeyPair (name):
    o = kernel.factory.KeyPair(name)
    return o

class _MountTarget:
	def __init__ (self, d):
		self.id = d['MountTargetId']
		self.idOwner = d['OwnerId']
		self.idFileSystem = d['FileSystemId']
		self.idSubnet = d['SubnetId']
		self.state = d['LifeCycleState']
		self.ipAddress = d['IpAddress']
		self.idNetworkInterface = d['NetworkInterfaceId']


def MountTarget (id):
	resp = Efs.client.describe_mount_targets(MountTargetId=id)
	hits = resp.get('MountTargets', None)
	hit = kernel.justOne(hits)
	o = _MountTarget(hit)
	return o


def NetworkInterface (id):
	o = kernel.factory.NetworkInterface(id)
	return o


def SecurityGroup (id):
	o = kernel.factory.SecurityGroup(id)
	return o


def Snapshot (id):
	o = kernel.snapshot.get(id)
	return o


def Subnet (id):
	o = kernel.subnet.get(id)
	return o


def Vault (name):
	accountId = '-'
	o = glacier.Vault(accountId, name)
	return o


def Volume (id):
    o = kernel.volume.get(id)
    return o
