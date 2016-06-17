import sys
from ec2Tools import waitFor

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python waitUntilRunning.py instanceId")
        sys.exit(-1)
    idInstance = sys.argv[1]
    waitFor.Instance(idInstance, 'instance_status_ok')
    
