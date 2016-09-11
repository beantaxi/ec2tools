from .tags import createTag 
from .tags import getName 
from .tags import getTag 
from .tags import nameInstance 
from .tags import nameVolume 
from .lifecycle import getStatus 
from .lifecycle import launchInstance 
from .addresses import associateAddress 
from .addresses import disassociateAddress 
from .glacier import uploadLargeFile

__all__ = ['createTag', 'getName', 'getTag', 'nameInstance', 'nameVolume', 'getStatus', 'launchInstance', 'associateAddress', 'disassociateAddress']
