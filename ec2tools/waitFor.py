import sys
from ._kernel import cli

def Instance (idInstance, forWhat):
	waiter = cli.get_waiter(forWhat)
	print("Waiting on {} for '{}'".format(idInstance, forWhat), file=sys.stderr)
	waiter.wait(InstanceIds=[idInstance])

def InstanceRunning (idInstance):
	Instance(idInstance, 'instance_running')


def InstanceStatusOk (idInstance):
	Instance(idInstance, 'instance_status_ok')


def Volume (idVolume, forWhat):
	waiter = cli.get_waiter(forWhat)
	print("Waiting on {} for '{}'".format(idVolume, forWhat), file=sys.stderr)
	waiter.wait(VolumeIds=[idVolume])


def VolumeAvailable (idVolume):
	Volume(idVolume, 'volume_available')


def VolumeInUse (idVolume):
	Volume(idVolume, 'volume_in_use')

