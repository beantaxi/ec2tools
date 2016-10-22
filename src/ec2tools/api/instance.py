from ec2tools import _kernel

def getNextAvailableDevice (instance):
	if isinstance(instance, str): instance = _kernel.getA.Instance(instance)
