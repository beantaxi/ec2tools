from . import Efs
from . import getA
from . import kernel
from .kernel import cli
from .kernel import factory
from .kernel import glacier


def getData (coll):
	all = coll.all()
	data = [o for o in all]
	return data


def Addresses ():
	resp = cli.describe_addresses()
	rawData = resp['Addresses']
	data = [getA.Address(el) for el in rawData]
	return data


def AvailabilityZones ():
	resp = cli.describe_availability_zones()
	rawData = resp['AvailabilityZones']
	data = [getA._AvailabilityZone(el) for el in rawData]
	return data


def ClassicAddresses ():
	data = getData(factory.classic_addresses)
	return data


def DhcpOptionsSets ():
	data = getData(factory.dhcp_options_sets)
	return data


def FileSystems ():
	resp = Efs.client.describe_file_systems()
	rawData = resp['FileSystems']
	data = [getA._FileSystem(el) for el in rawData]
	return data


def Images ():
	data = getData(factory.images)
	return data


def Instances ():
	data = kernel.instance.all()
	return data


def InternetGateways ():
	data = getData(factory.internet_gateways)
	return data 


def KeyPairs ():
	data = getData(factory.key_pairs)
	return data


def NetworkAcls ():
	data = getData(factory.network_acls)
	return data


def NetworkInterfaces ():
    data = getData(factory.network_interfaces)
    return data 


def PlacementGroups ():
	data = getData(factory.placement_groups)
	return data


def RouteTables ():
	data = getData(factory.route_tables)
	return data


def SecurityGroups ():
	data = getData(factory.security_groups)
	return data


def Snapshots ():
	data = getData(factory.snapshots)
	return data


def Subnets ():
	data = kernel.subnet.all()
	return data


def Vaults ():
	data = getData(glacier.vaults)
	return data


def Volumes ():
	data = kernel.volume.all()
	return data 


def Vpcs ():
	data = getData(factory.vpcs)	
	return data


def VpcAddresses ():
	data = getData(factory.vpc_addresses)
	return data


def VpcPeeringConnections ():
	data = getData(factory.vpc_peering_connections)
	return data


