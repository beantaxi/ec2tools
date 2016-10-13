#!/bin/bash
    
if [ $# -lt 3 ]; then
	>&2 echo Usage: python3 ${FUNCNAME[0]} name keyName IP
	sys.exit(-1)

name=$1
keyName=$2
ip=$3

PYPATH=${PYPATH:-python3}
$PYPATH -c "import ec2tools; ec2tools.api.launchInstance(name='$name', keyName='$keyName', securityGroup='setup', )"


from pprint import pprint as pp
import sys
from sparktools import Ec2

if __name__ == '__main__':
	if len(sys.argv) < 4:
		print("Usage: python3 launchEc2Instance.py name keyName IP")
		sys.exit(-1)
	name = sys.argv[1]
	keyName = sys.argv[2]
	ip = sys.argv[3]
	ec2 = Ec2("us-west-2")
	
	print("Disassociating {}... ".format(ip))
	resp = ec2.disassociateAddress(ip)
	pp(resp)
	print("Creating {} with keypair '{}'... ".format(name, keyName))
	idInstance = ec2.launchInstance(name=name, keyName=keyName)
	print("Waiting until instance is running... ")
	ec2.waitUntilRunning(idInstance)
	print("Associating {} to instance... ".format(ip))
	ec2.associateAddress(ip=ip, instanceId=idInstance)
	print("EC2 Instance {} ({}) Created".format(name, ip))

