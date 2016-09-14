from . import allThe
from . import api

def Snapshot (*, name):
	if not name:
		raise Exception("Please specify a name")
	data = allThe.Snapshots()
	hits = [o for o in data if api.getName(o) == name]
	hit = None
	if hits:
		if len(hits) > 1:
			raise Exception("Multiple snapshots found")
		else:
			hit = hits[0]
	return hit

def Instance (*, name=None, hostname=None, ip=None):
	data = allThe.Instances()
	if name:
		hits = [o for o in data if api.getName(o) == name]
	elif ip:
		hits = [o for o in data if o.public_ip_address == ip]
	elif hostname:
		hits = [o for o in data if o.public_dns_name == hostname]
	else:
		raise Exception('Instance() called with no arguments')
	hit = None
	if hits:
		if len(hits) > 1:
			raise Exception("Multiple instances found")
		else:
			hit = hits[0]
	return hit
