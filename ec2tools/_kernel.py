import boto3

# Shared variables
cli = boto3.client("ec2")
factory = boto3.resource("ec2")
