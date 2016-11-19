import io
import os.path
import sys
from ec2tools.kernel import factory

def importPublicKey (name, path):
	if not os.path.exists(path):
		print("Key file '{}' not found".format(path))
		sys.exit(1)
	f = open(path, 'rb', buffering=0)
	data = f.readall()
	factory.import_key_pair(KeyName=name, PublicKeyMaterial=data)
