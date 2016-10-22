from ec2tools import _kernel, api, getA

def createVolume (snapshot, availabilityZone, volumeType='gp2'):
	if isinstance(snapshot, str): snapshot = getA.Snapshot(snapshot)
	idSnapshot = snapshot.id
	snapshotName = _kernel.getName(snapshot)
	if volumeType == 'io1':
		iops = 30*snapshot.volume_size    # The maximum allowable
		volume = _kernel.factory.create_volume(SnapshotId=idSnapshot, AvailabilityZone=availabilityZone, VolumeType=volumeType, Iops=iops)
	else:
		volume = _kernel.factory.create_volume(SnapshotId=idSnapshot, AvailabilityZone=availabilityZone, VolumeType=volumeType)
	_kernel.setName(volume, snapshotName)
	return volume
