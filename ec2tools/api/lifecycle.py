from ec2tools._kernel import cli 

def getStatus (o):
	status = o.state['Name']
	return status


def launchInstance (*, name, keyName, imageId, instanceType, securityGroup):
	resp = cli.run_instances(ImageId=imageId, 
	                              MinCount=1, MaxCount=1,
		                           KeyName=keyName,
		                           SecurityGroups=[securityGroup],
		                           InstanceType=instanceType)
	id = resp['Instances'][0]['InstanceId']
	nameInstance(id, name)
	return id
