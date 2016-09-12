from . import allThe
from . import api

def _addNames (data, tagsFieldName='tags'):
	for o in data:
		name = api.getName(o, tagsFieldName)
		o.__setattr__('name', name)

def _addStatuses (data):
	for o in data:
		status = api.getStatus(o)
		o.__setattr__('status', status)


def _listData (data, fieldNames):
	print(fieldNames)
	fieldNameList = [fieldName.strip() for fieldName in fieldNames.split(',')]
	braces = ','.join(['{}'] * len(fieldNameList))
	for o in data:
		args = []
		for fieldName in fieldNameList:
			args.append(o.__getattribute__(fieldName))
		print(braces.format(*args))


def Addresses ():
	data = allThe.Addresses()
	fields = "public_ip,allocation_id,instance_id,association_id,domain,private_ip_address"
	_listData(data, fields)


def Instances ():
	data = allThe.Instances()
	_addNames(data)
	_addStatuses(data)
	fields = "id,name,status,public_ip_address"
	_listData(data, fields)


def InternetGateways ():
	data = allThe.InternetGateways()
	_addNames(data)
	fields = "id,name"
	_listData(data, fields)


def KeyPairs ():
	data = allThe.KeyPairs()
	fields = "name,key_name,key_fingerprint"
	_listData(data, fields)


def NetworkInterfaces ():
	data = allThe.NetworkInterfaces()
	_addNames(data, "tag_set")
	fields = "id,name,subnet_id,vpc_id"
	_listData(data, fields)


def SecurityGroups ():
	data = allThe.SecurityGroups()
	fields = "id,group_name,description"
	_listData(data, fields)


def Snapshots ():
	data = allThe.Snapshots()
	_addNames(data)
	fields = "id,name,volume_size,state,volume_id,owner_id,start_time,progress"
	_listData(data, fields)


def Vaults ():
	data = allThe.Vaults()
	fields = "name, creation_date, last_inventory_date, size_in_bytes, number_of_archives"
	_listData(data, fields)


def Volumes ():
	data = allThe.Volumes()
	_addNames(data)
	fields = "id,name,size,availability_zone"
	_listData(data, fields)
