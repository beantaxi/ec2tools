from . import allThe
from . import api

def Addresses ():
	data = allThe.Addresses()
	print("public_ip", "allocation_id", "instance_id", "association_id", "domain", "private_ip_address")
	for d in data:
		print("{},{},{},{},{},{}".format(d.get('PublicIp'), d.get('AllocationId'), d.get('InstanceId'), d.get('AssociationId'), d.get('Domain'), d.get('PrivateIpAddress')))


def Instances ():
	data = allThe.Instances()
	print("id,name,status")
	for o in data:
		name = api.getName(o)
		status = api.getInstanceStatus(o)
		print("{},{},{},{},{}".format(o.id, name, status, o.launch_time, o.public_ip_address))


def KeyPairs ():
	pass


def SecurityGroups ():
	data = allThe.SecurityGroups()
	print("id,name,description")
	for o in data:
		print("{},{},{}".format(o.group_id, o.group_name, o.description))


def Volumes ():
	data = allThe.Volumes()
	print("id,name,size,availabilityZone")
	for o in data:
		name = api.getName(o)
		print("{},{},{},{},{}".format(o.id, name, o.size, o.availability_zone, o.create_time))
