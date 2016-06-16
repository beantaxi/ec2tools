import boto3
from pprint import pprint as pp
import sys
import ec2tools

if __name__ == '__main__':
    data = ec2.all.securityGroups()    
    for row in data:
        print('{:20}{:13}{}'.format(row.group_name, row.group_id, row.description))
