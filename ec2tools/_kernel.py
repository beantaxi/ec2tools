import boto3

# Shared variables
cli = boto3.client("ec2")
factory = boto3.resource("ec2")

def toList (*args):
    if not isinstance(args, list):
        args = list(args)
    if len(args) == 1 and isinstance(args[0], list):
        args = args[0]
    return args

