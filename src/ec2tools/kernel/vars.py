import boto3

# Shared variables
cli = boto3.client("ec2")
factory = boto3.resource("ec2")
glacier = boto3.resource("glacier")
iam = boto3.resource("iam")

