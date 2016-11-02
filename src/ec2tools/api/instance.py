from ec2tools import getA 

def getNextAvailableDevice (instance):
	if isinstance(instance, str): instance = getA.Instance(instance)
