from ec2tools import kernel

def getMySnapshots ():
	# We *can* get this by filtering on the service resource's snapshots member (rather, it's all() method). But it is much slower.
	myId=kernel.getAccountId()
	ownerIds = [myId]
	data = kernel.factory.snapshots.filter(OwnerIds=ownerIds)
	mySnapshots = [o for o in data]
	return mySnapshots
