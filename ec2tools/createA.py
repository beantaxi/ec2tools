import boto3

def Volume (*, size, availabilityZone, volumeType):
	cli = boto3.resource("ec2", "us-west-2")
	resp = cli.create_volume(Size=size, AvailabilityZone=availabilityZone, VolumeType=volumeType)
	return resp
