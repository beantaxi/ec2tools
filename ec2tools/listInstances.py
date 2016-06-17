import boto3
from pprint import pprint as pp
import sys
import ec2tools

if __name__ == '__main__':
    data = ec2tools.allThe.Instances()
    for instance in data:
        print("{:14}{:20}{}", instance.id, instance.public_ip_address, instance.state)
