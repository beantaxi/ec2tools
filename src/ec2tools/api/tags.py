from ec2tools import _kernel


def nameInstance (idInstance, name):
	instance = _kernel.factory.Instance(idInstance)
	resp = _kernel.createTag(instance, 'Name', name)
	return resp


def nameVolume (idVolume, name):
	volume = _kernel.factory.Volume(idVolume)
	resp = _kernel.createTag(volume, 'Name', name)
	return resp








