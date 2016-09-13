from ._kernel import cli
from ._kernel import glacier


def Vault (name):
	vault = glacier.create_vault(vaultName=name)
	return vault


def Volume (*, size, availabilityZone, volumeType):
	resp = cli.create_volume(Size=size, AvailabilityZone=availabilityZone, VolumeType=volumeType)
	return resp
