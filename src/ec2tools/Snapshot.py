from ec2tools import kernel, api, getA

def createVolume (snapshot, availabilityZone, volumeType='gp2'):
	if isinstance(snapshot, str): snapshot = getA.Snapshot(snapshot)
	idSnapshot = snapshot.id
	snapshotName = kernel.getName(snapshot)
	if volumeType == 'io1':
		iops = 30*snapshot.volume_size    # The maximum allowable
		volume = kernel.factory.create_volume(SnapshotId=idSnapshot, AvailabilityZone=availabilityZone, VolumeType=volumeType, Iops=iops)
	else:
		volume = kernel.factory.create_volume(SnapshotId=idSnapshot, AvailabilityZone=availabilityZone, VolumeType=volumeType)
	kernel.setName(volume, snapshotName)
	return volume
