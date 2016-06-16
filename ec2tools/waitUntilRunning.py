import boto3
import sys

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python waitUntilRunning.py instanceId")
        sys.exit(-1)
    idInstance = sys.argv[1]
    cli = boto3.client('ec2', 'us-west-2')
    waiter = cli.get_waiter('instance_running')
    print("Waiting till {} is running... ").format(idInstance))
    waiter.wait(idInstance)
    
