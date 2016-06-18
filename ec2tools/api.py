import sys
from ._kernel import cli
from ._kernel import factory
from ._kernel import iam
from . import allThe

def associateAddress (*, ip, idInstance):
	addrs = allThe.Addresses()
	allocationId = _getAllocationIdByIp(addrs, ip)
	resp = cli.associate_address(InstanceId=idInstance, AllocationId=allocationId)
	return resp


def disassociateAddress (ip):
	addrs = allThe.Addresses()
	id = _getAssociationIdByIp(addrs, ip)
	resp = cli.disassociate_address(AssociationId=id) if id else None
	return resp


def createTag (resource, key, value):
	tag = {'Key': key, 'Value': value}
	tags = [tag]
	resp = resource.create_tags(Tags=tags)
	return resp


def getInstanceStatus (instance):
	status = instance.state['Name']
	return status


def getName (resource):
	nameTag = getTag(resource, "Name")
	name = nameTag['Value'] if nameTag else None
	return name


def getTag (resource, tagName):
	tags = resource.tags
	matches = [tag for tag in tags if tag['Key'] == tagName] if tags else []
	if len(matches) > 1:
		raise(Exception("More than one matching tag"))
	tag = matches[0] if matches else None
	return tag


def launchInstance (*, name, keyName, imageId, instanceType, securityGroup):
	resp = cli.run_instances(ImageId=imageId, 
	                              MinCount=1, MaxCount=1,
		                           KeyName=keyName,
		                           SecurityGroups=[securityGroup],
		                           InstanceType=instanceType)
	id = resp['Instances'][0]['InstanceId']
	nameInstance(id, name)
	return id


def nameInstance (idInstance, name):
	instance = factory.Instance(idInstance)
	resp = createTag(instance, 'Name', name)


def nameVolume (idVolume, name):
	volume = factory.Volume(idVolume)
	resp = createTag(volume, 'Name', name)
	return resp


def _getAllocationIdByIp (addresses, ip):
	rs = [a for a in addresses if a['PublicIp'] == ip]
	allocationId = rs[0].get('AllocationId') if rs else None
	return allocationId
	
	
def _getAssociationIdByIp (addresses, ip):
	rs = [a for a in addresses if a['PublicIp'] == ip]
	assocationId = rs[0].get('AssociationId') if rs else None
	return assocationId

