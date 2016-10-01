import boto3
import botocore.utils
import io
import math
import numbers
import os.path
from ec2tools import getA

ONE_MEG = 1<<20
ONE_GIG = 1<<30
MIN_CHUNK = ONE_MEG
MAX_CHUNK = 4*ONE_GIG


######################################################################
#
# This is a generator which yields chunks from a file, one chunkSize
# at a time.
#
# This gets a bit weird, because the Boto3 Glacier API is expecting the 
# chunk as a file-like object (even though the docs say otherwise).
# So we need to read the data a chunk at a time into the bytearray,
# and then create a BytesIO out of the bytearray, and return the BytesIO
# as our chunk.
#




def genChunk (f, chunkSize):
	chunkSize = validateChunkSize(chunkSize)
	# Create buffer
	buf = bytearray(chunkSize)
	iStart = 0
	nRead = 0
	while True:
		iStart = iStart+nRead
		nRead = f.readinto(buf)
		if not nRead:
			break
		iEnd = iStart+nRead-1
		range = "bytes {}-{}/*".format(iStart, iEnd)
		data = buf[:nRead]
		body = io.BytesIO(data)
		yield {'body': body, 'range': range, 'data': data, 'iStart': iStart, 'iEnd': iEnd}	


#######################################################################
#
#   We want 100 chunks or less
#
# So we want the smallest chunk size, where 
#
#    chunkSize*100 >= totalSize
#
# And since
#
#    chunkSize = 2^n*1M
#
#  for some n, we have
#
#    2^n*1M*100 >= totalSize
#
#  Setting k=1M*100, we have
#    2^n*k>= totalSize
#    2^n >= totalSize/k
#    n >= log(totalSize/k, 2)
#    n = ceil(log(totalSize/k, 2))
#
#  And then plugging n into the above
#   
#    chunkSize = 2^n*1M
#
#  gives us our chunkSize. Which we then need to clip to the Min and Max values.
#  Convert it to int, and we're good to go
#
def getChunkSize (totalSize):
	k = ONE_MEG*100
	x = totalSize/k
	y = math.log(x, 2)
	n = math.ceil(y)
	rawChunkSize = math.pow(2, n) * ONE_MEG
	chunkSize = int(min(MAX_CHUNK, max(rawChunkSize, MIN_CHUNK)))

	return chunkSize


#######################################################################
#
# Chunk size validation rules:
#
#   Minimum chunk size = 1M
#   Maximum chunk size = 4G
#   Chunk size must be 1M, 2M, 4M, 8M etc: "a meg times a power of 2"
#
def validateChunkSize (chunkSize):
	if not isinstance(chunkSize, numbers.Number) or chunkSize-int(chunkSize) != 0:
		raise Exception("{} must a number, and convertible to an integer".format(chunkSize))
	chunkSize = int(chunkSize)
	if chunkSize < MIN_CHUNK or chunkSize > MAX_CHUNK:
		raise Exception("{} must be between {} or {}".format(chunkSize, MIN_CHUNK, MAX_CHUNK))
	if not math.log(chunkSize/ONE_MEG, 2).is_integer():
		raise Exception("{} must be 1M times a power of 2 (1M, 2M, 4M, 8M, etc)".format(chunkSize))
	return chunkSize	




#######################################################################
#
# Upload a large
#

def uploadLargeFile (path, vaultName, archiveName=None, chunkSize=None):
	if not os.path.exists(path): raise Exception("{} does not exist".format(path))	     # Validate that file exists
	if not os.path.isfile(path): raise Exception("{} is not a file".format(path))         # Validate it's a file
	fileSize = os.path.getsize(path)
	if filesize < MIN_SIZE: raise Exception("File size must be >= {}".format(MIN_SIZE))   # Validate the file is not too small for multipart

	f = io.FileIO(path, 'rb')
	vault	= getA.Vault(vaultName)
	qq	
	# Validate vault exists
	if not archiveName:
		archiveName = os.path.basename(path)
	if not chunkSize:
		chunkSize = getChunkSize(fileSize)
	else:
		chunkSize = validateChunkSize(chunkSize)
	multi = vault.initiate_multipart_upload(archiveDescription=archiveName, partSize=str(chunkSize))
	for chunk in genChunk(f, chunkSize):
		fChunk = io.BytesIO(chunk)                                                        # Glacier is expecting a file-like object, not a bytearray
		print("Uploading {} to {} ...".format(chunk['iStart'], chunk['iEnd']))
		multi.upload_part(body=chunk['body'], range=chunk['range'])
	print("Done.")
	size = chunk['iEnd']+1
	checksum = botocore.utils.calculate_tree_hash(io.FileIO(path, 'rb'))
	resp = multi.complete(archiveSize=str(size), checksum=checksum)
	return resp
