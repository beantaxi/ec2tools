from ._kernel import cli

def Volume (*, size, availabilityZone, volumeType):
	resp = cli.create_volume(Size=size, AvailabilityZone=availabilityZone, VolumeType=volumeType)
	return resp
