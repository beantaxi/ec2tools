from ._kernel import cli
from ._kernel import factory

def getData (elementName, idName, fnDescribe, fnFactory):
    resp = fnDescribe()
    rawData = resp[elementName]
    ids = [r[idName] for r in rawData]
    data = [fnFactory(id) for id in ids]
    return data


def Addresses ():
	resp = cli.describe_addresses()
	data = resp['Addresses']
	return data


def Instances ():
    resp = cli.describe_instances()
    rawData = resp['Reservations']
    ids = []
    for row in rawData:
        instances = row['Instances']
        for instance in instances:
            id = instance['InstanceId']
            ids.append(id)
    data = [factory.Instance(id) for id in ids]
    return data


def KeyPairs ():
    resp = cli.describe_key_pairs()
    rawData = resp['KeyPairs']
    data = [factory.KeyPair(r['KeyName']) for r in rawData]
    return data


def SecurityGroups ():
    data = getData('SecurityGroups', 'GroupId', cli.describe_security_groups, factory.SecurityGroup)
    return data 


def Volumes ():
    data = getData('Volumes', 'VolumeId', cli.describe_volumes, factory.Volume)
    return data 
