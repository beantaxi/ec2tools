import boto3

class Ec2:
    def __init__ (self, regionName):
        self.regionName = regionName
        self.cli = boto3.client('ec2', regionName)

