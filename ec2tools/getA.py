from ._kernel import factory

def Address (d):
	if d['Domain'] == 'classic':
		id = d['PublicIp']
		o = factory.ClassicAddress(id)
	elif d['Domain'] == 'vpc':
		id = d['AllocationId']
		o = factory.VpcAddress(id)
	else:
		raise Exception("Unknown address type: '{}'".format(d['Domain']))
	return o


def Instance (id):
    o = factory.Instance(id)
    return o


def InternetGateway (id):
    o = factory.InternetGateway(id)
    return o


def KeyPair (name):
    o = factory.KeyPair(name)
    return o


def NetworkInterface (id):
	o = factory.NetworkInterface(id)
	return o


def SecurityGroup (id):
	o = factory.SecurityGroup(id)
	return o


def Snapshot (id):
	o = factory.Snapshot(id)
	return o


def Volume (id):
    o = factory.Volume(id)
    return o

 
