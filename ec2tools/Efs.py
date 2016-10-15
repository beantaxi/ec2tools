import boto3
import uuid
from . import getA
from . import _kernel

client = boto3.client('efs')


def createFileSystem (name=None, mode='generalPurpose'):
	if name is None:	                                                                                 # Respect blank names - a blank name is a name!
		name = str(uuid.uuid4())                                                                        # Generate a random UUID
	resp = client.create_file_system(CreationToken=name, PerformanceMode=mode)
	id = resp['FileSystemId']
	tag = {'Key': 'Name', 'Value': name}
	tags = [tag]
	client.create_tags(FileSystemId=id, Tags=tags)
	return id


def createMountTarget (idFileSystem, idSubnet):
	resp = client.create_mount_target(FileSystemId=idFileSystem, SubnetId=idSubnet)
	id = resp['MountTargetId']
	return id


def getMountTargets (fileSystem):
	idFileSystem = _kernel.getId(fileSystem)
	resp = client.describe_mount_targets(FileSystemId=idFileSystem)
	rawData = resp['MountTargets']
	mountTargets = [getA._MountTarget(d) for d in rawData]
	return mountTargets
