import sys
from ._kernel import cli

def Instance (idInstance, forWhat):
	waiter = cli.get_waiter(forWhat)
	waiter.wait(InstanceIds=[idInstance])

def InstanceRunning (idInstance):
	Instance(idInstance, 'instance_running')


def InstanceStatusOk (idInstance):
	Instance(idInstance, 'instance_status_ok')


def Volume (idVolume, forWhat):
	waiter = cli.get_waiter(forWhat)
	waiter.wait(VolumeIds=[idVolume])


def VolumeAvailable (idVolume):
	Volume(idVolume, 'volume_available')


def VolumeInUse (idVolume):
	Volume(idVolume, 'volume_in_use')

