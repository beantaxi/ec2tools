import boto3
import botocore.utils
import io
import math
import os.path
from ec2tools import getA

def genChunk (f, chunk_size):
	# Create buffer
	buf = bytearray(chunk_size)
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
# The rules:
#
#   Minimum chunk size = 1M
#   Maximum chunk size = 4G
#   Chunk size must be 1M, 2M, 4M, 8M etc: "a meg times a power of 2"
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
#  gives us our chunksize. Which we then need to clip to the Min and Max values.
#
#  Solution: use log base 2, to get the chunk size that sneaks us under 100
#    chunks, unless nData > 100*MAX_CHUNK
#
def getChunkSize (totalSize):
	ONE_MEG = 1<<20
	ONE_GIG = 1<<30
	MIN_CHUNK = ONE_MEG
	MAX_CHUNK = 4*ONE_GIG

	k = ONE_MEG*100
	x = totalSize/k
	y = math.log(x, 2)
	n = math.ceil(y)
	rawChunkSize = math.pow(2, n) * ONE_MEG
	chunkSize = min(MAX_CHUNK, max(rawChunkSize, MIN_CHUNK))
	return chunkSize


def uploadLargeFile (path, vaultName, archiveName=None, chunkSize=None):
	# Validate that file exists
	# Validate value exists
	# Validate chunksize is legit
	if not archiveName:
		archiveName = os.path.basename(path)
	if not chunkSize:
		fileSize = os.path.getsize(path)
		chunkSize = getChunkSize(fileSize)
	vault	= getA.Vault(vaultName)
	multi = vault.initiate_multipart_upload(archiveDescription=archiveName, partSize=str(chunkSize))
	f = io.FileIO(path, 'rb')
	for chunk in genChunk(f, chunkSize):
		print("Uploading {} to {} ...".format(chunk['iStart'], chunk['iEnd']))
		multi.upload_part(body=chunk['body'], range=chunk['range'])
	print("Done.")
	size = chunk['iEnd']+1
	checksum = botocore.utils.calculate_tree_hash(io.FileIO(path, 'rb'))
	resp = multi.complete(archiveSize=str(size), checksum=checksum)
	return resp
