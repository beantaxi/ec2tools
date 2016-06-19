from . import _kernel
from . import getA
from ._kernel import cli

def getData (elementName, idName, fnDescribe, fnFactory):
    resp = fnDescribe()
    rawData = resp[elementName]
    ids = [r[idName] for r in rawData]
    data = [fnFactory(id) for id in ids]
    return data


def Addresses ():
	resp = cli.describe_addresses()
	rawData = resp['Addresses']
	data = [getA.Address(d) for d in rawData]
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
    data = [getA.Instance(id) for id in ids]
    return data


def InternetGateways ():
    data = getData('InternetGateways', 'InternetGatewayId', cli.describe_internet_gateways, getA.InternetGateway)
    return data 


def KeyPairs ():
    resp = cli.describe_key_pairs()
    rawData = resp['KeyPairs']
    data = [getA.KeyPair(r['KeyName']) for r in rawData]
    return data


def NetworkInterfaces ():
    data = getData('NetworkInterfaces', 'NetworkInterfaceId', cli.describe_network_interfaces, getA.NetworkInterface)
    return data 


def SecurityGroups ():
    data = getData('SecurityGroups', 'GroupId', cli.describe_security_groups, getA.SecurityGroup)
    return data 


def Snapshots ():
	ownerId = _kernel.getCurrentOwnerId()
	resp = cli.describe_snapshots(OwnerIds=[ownerId])
	rawData = resp['Snapshots']
	data = [getA.Snapshot(d['SnapshotId']) for d in rawData]
	return data


def Volumes ():
    data = getData('Volumes', 'VolumeId', cli.describe_volumes, getA.Volume)
    return data 
