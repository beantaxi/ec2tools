from . import misc
from .vars import cli

class _AvailabilityZone:
	def __init__ (self, d):
		self.name = d['ZoneName']
		self.state = d['State']
		self.region = d['RegionName']
		self.messages = [m['Message'] for m in d['Messages']]


def get (name):
	zoneNames = [name]
	resp = cli.describe_availability_zones(ZoneNames=zoneNames)
	rawData = resp['AvailabilityZones']
	d = misc.justOne(rawData)
	o = _AvailabilityZone(d)
	return o

