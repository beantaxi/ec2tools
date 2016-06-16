import boto3

cli = boto3.client('ec2', 'us-west-2')
factory = boto3.resource('ec2', 'us-west-2')


def Instance (id):
    o = factory.Instance(id)
    return o

def KeyPair (name):
    o = factory.KeyPair(name)
    return o


def Volume (id):
    o = factory.Volume(id)
    return o
