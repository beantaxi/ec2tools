from ec2tools import _kernel


def getMySnapshots ():
	# We *can* get this by filtering on the service resource's snapshots member (rather, it's all() method). But it is much slower.
	myId=_kernel.getAccountId()
	ownerIds = [myId]
	data = _kernel.factory.snapshots.filter(OwnerIds=ownerIds)
	mySnapshots = [o for o in data]
	return mySnapshots
