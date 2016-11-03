from ec2tools import getA 

def createInstance (*, name, keyName, imageId, instanceType, securityGroup):
	instance = createAndRun(name=name, keyName=keyName, imageId=imageId, instanceType=instanceType, securityGroup=securityGroup)
	print("Waiting for instance.running... ")
	waitFor.InstanceRunning(instance.id)
	instance.stop()
	print("Waiting for instance.stopped... ")
	waitFor.InstanceStopped(instance.id)
	return instance


def createAndRunInstance (*, name, keyName, imageId, instanceType, securityGroup):
	instances = kernel.factory.create_instances(ImageId=imageId, 
 	                                             MinCount=1, MaxCount=1,
 	                                             KeyName=keyName,
 	                                             SecurityGroups=[securityGroup],
 	                                             InstanceType=instanceType)
	instance = kernel.justOne(instances)
	kernel.setName(instance, name)
	return instance
