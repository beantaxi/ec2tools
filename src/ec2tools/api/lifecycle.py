from ec2tools.kernel import cli 
from ec2tools.api import tags

def launchInstance (*, name, keyName, imageId, instanceType, securityGroup):
	resp = cli.run_instances(ImageId=imageId, 
	                              MinCount=1, MaxCount=1,
		                           KeyName=keyName,
		                           SecurityGroups=[securityGroup],
		                           InstanceType=instanceType)
	id = resp['Instances'][0]['InstanceId']
	tags.nameInstance(id, name)
	return id