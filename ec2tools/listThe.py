from . import allThe
from . import api

def listStuff (data, fields):
	print(fields)
	fieldList = fields.split(',')
	braces = ','.join(['{}'] * len(fieldList))
	for o in data:
		args = []
		for f in fieldList:
			args.append(o.__getattribute__(f))
		print(braces.format(*args))


def Addresses ():
	data = allThe.Addresses()
	fields = "public_ip,allocation_id,instance_id,association_id,domain,private_ip_address"
	listStuff(data, fields)


def Instances ():
	data = allThe.Instances()
	for o in data:
		name = api.getName(o)
		status = api.getInstanceStatus(o)
		o.__setattr__('name', name)
		o.__setattr__('status', status)
	fields = "id,name,status"
	listStuff(data, fields)


def KeyPairs ():
	data = allThe.KeyPairs()
	fields = "name,key_name,key_fingerprint"
	listStuff(data, fields)


def SecurityGroups ():
	data = allThe.SecurityGroups()
	for o in data:
		name = api.getName(o)
		o.__setattr__('name', name)
	fields = "id,name,description"
	listStuff(data, fields)


def Snapshots ():
	data = allThe.Snapshots()
	for o in data:
		name = api.getName(o)
		o.__setattr__('name', name)
	fields = "id,name,volume_size,state,volume_id,owner_id,start_time,progress"
	listStuff(data, fields)


def Volumes ():
	data = allThe.Volumes()
	for o in data:
		name = api.getName(o)
		o.__setattr__('name', name)
	fields = "id,name,size,availability_zone"
	listStuff(data, fields)
