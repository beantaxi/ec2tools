from . import kernel, allThe


def _addNames (data, tagsFieldName='tags'):
	for o in data:
		name = kernel.getName(o, tagsFieldName)
		o.__setattr__('name', name)

def _addStatuses (data):
	for o in data:
		status = kernel.getStatus(o)
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


def Addresses (data=None):
	if data == None:
		data = allThe.Addresses()
	fields = "public_ip,allocation_id,instance_id,association_id,domain,private_ip_address"
	_listData(data, fields)


def AvailabilityZones (data=None):
	if data == None:
		data = allThe.AvailabilityZones()
	fields = "name, region, state"
	_listData(data, fields)


def FileSystems (data=None):
	if data == None:
		data = allThe.FileSystems()
	fields = "id,name,state,mountTargetCount,size"
	_listData(data, fields)


def Instances (data=None):
	if data == None:
		data = allThe.Instances()
	fields = "id,name,status,public_ip_address"
	_listData(data, fields)


def InternetGateways (data=None):
	if data == None:
		data = allThe.InternetGateways()
	_addNames(data)
	fields = "id,name"
	_listData(data, fields)


def KeyPairs (data=None):
	if data == None:
		data = allThe.KeyPairs()
	fields = "name,key_name,key_fingerprint"
	_listData(data, fields)


def NetworkInterfaces (data=None):
	if data == None:
		data = allThe.NetworkInterfaces()
	_addNames(data, "tag_set")
	fields = "id,name,subnet_id,vpc_id"
	_listData(data, fields)


def SecurityGroups (data=None):
	if data == None:
		data = allThe.SecurityGroups()
	fields = "id,group_name,description"
	_listData(data, fields)


def Snapshots (data=None):
	if data == None:
		data = allThe.Snapshots()
	_addNames(data)
	fields = "id,name,volume_size,state,volume_id,owner_id,start_time,progress"
	_listData(data, fields)


def Subnets (data=None):
	if data == None:
		data = allThe.Subnets()
	_addNames(data)
	fields = "id, cidr_block, availability_zone, vpc_id, default_for_az, state"
	_listData(data, fields)


def Vaults (data=None):
	if data == None:
		data = allThe.Vaults()
	fields = "name, creation_date, last_inventory_date, size_in_bytes, number_of_archives"
	_listData(data, fields)


def Volumes (data=None):
	if data == None:
		data = allThe.Volumes()
	_addNames(data)
	fields = "id,name,size,availability_zone"
	_listData(data, fields)


def Vpcs (data=None):
	if data == None:
		data = allThe.Vpcs()
	_addNames(data)
	fields="id, name, state, is_default, cidr_block"
	_listData(data, fields)
