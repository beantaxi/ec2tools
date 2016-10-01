from ec2tools._kernel import cli 
from ec2tools import allThe

def associateAddress (*, ip, idInstance):
	addrs = allThe.Addresses()
	allocationId = _getAllocationIdByIp(addrs, ip)
	resp = cli.associate_address(InstanceId=idInstance, AllocationId=allocationId)
	return resp


def disassociateAddress (ip):
	addrs = allThe.Addresses()
	id = _getAssociationIdByIp(addrs, ip)
	resp = cli.disassociate_address(AssociationId=id) if id else None
	return resp


def _getAllocationIdByIp (addresses, ip):
	rs = [a for a in addresses if a.public_ip == ip]
	allocationId = rs[0].allocation_id if rs else None
	return allocationId
	
	
def _getAssociationIdByIp (addresses, ip):
	rs = [a for a in addresses if a.public_ip == ip]
	assocationId = rs[0].association_id if rs else None
	return assocationId
