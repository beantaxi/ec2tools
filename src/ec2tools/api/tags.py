from ec2tools import kernel


def nameInstance (idInstance, name):
	instance = kernel.factory.Instance(idInstance)
	resp = kernel.createTag(instance, 'Name', name)
	return resp


def nameVolume (idVolume, name):
	volume = kernel.factory.Volume(idVolume)
	resp = kernel.createTag(volume, 'Name', name)
	return resp








