import boto3

def Instance (idInstance, forWhat):
	cli = boto3.client('ec2', 'us-west-2')
	waiter = cli.get_waiter(forWhat)
	print("Waiting on {} for '{}'".format(idInstance, forWhat))
	waiter.wait(InstanceIds=[idInstance])


def Volume (idVolume, forWhat):
	cli = boto3.client('ec2', 'us-west-2')
	waiter = cli.get_waiter(forWhat)
	print("Waiting on {} for '{}'".format(idVolume, forWhat))
	waiter.wait(VolumeIds=[idVolume])


def VolumeAvailable (idVolume):
	Volume(idVolume, 'volume_available')


def VolumeInUse (idVolume):
	Volume(idVolume, 'volume_in_use')

