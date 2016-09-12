from . import allThe
from ec2tools import api

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
	if hits:
		if len(hits) > 1:
			raise Exception("Multiple instances found")
		else:
			instance = hits[0]
	else:
		instance = None
	return instance
