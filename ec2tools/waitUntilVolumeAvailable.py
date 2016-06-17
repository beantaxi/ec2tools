import sys
from ec2tools import waitFor

if __name__ == '__main__':
	if len(sys.argv) < 2:
		import os.path
		print("Usage: python {} idVolume".format(os.path.basename(__file__)))
		sys.exit(-1)
	idVolume = sys.argv[1]
	waitFor.VolumeAvailable(idVolume)

    
