from . import kernel, allThe

def Instance (*, name=None, hostname=None, ip=None):
	data = allThe.Instances()
	if name:
		hits = [o for o in data if kernel.getName(o) == name]
	elif ip:
		hits = [o for o in data if o.public_ip_address == ip]
	elif hostname:
		hits = [o for o in data if o.public_dns_name == hostname]
	else:
		raise Exception('Instance() called with no arguments')
	instance = kernel.justOneOrNone(hits)
	return instance


def SecurityGroup (*, name):
	if not name:
		raise Exception("Please specify a name")
	data = allThe.SecurityGroups()
	hits = [o for o in data if o.group_name == name]
	hit = kernel.justOneOrNone(hits)
	return hit


def Snapshot (*, name):
	if not name:
		raise Exception("Please specify a name")
	data = allThe.Snapshots()
	hits = [o for o in data if kernel.getName(o) == name]
	hit = kernel.justOneOrNone(hits)
	return hit


def Volume (*, name):
	if not name:
		raise Exception("Please specify a name")
	data = allThe.Volumes()
	hits = [o for o in data if kernel.getName(o) == name]
	hit = kernel.justOneOrNone(hits)
	return hit
