from .efs import createFileSystem
from .efs import deleteFileSystem
from .efs import getMountTargetForInstance 
from .efs import getMountUrl
from .lifecycle import launchInstance 
from .addresses import associateAddress 
from .addresses import disassociateAddress 
from .glacier import uploadLargeFile
from .instance import getNextAvailableDevice
from .snapshot import getMySnapshots
from .tags import nameInstance
from .tags import nameVolume

__all__ = ['createFileSystem', 'deleteFileSystem', 'getMountTargetForInstance', 'getMountUrl', 'createTag', 'getTag', 'nameInstance', 'nameVolume', 'launchInstance', 'associateAddress', 'disassociateAddress', 'uploadLargeFile', 'getDevices', 'getNextAvailableDevice', 'getMySnapshots']
