from ec2tools import allThe

if __name__ == '__main__':
    data = allThe.Instances()
    for instance in data:
        print("{:14}{:20}{}", instance.id, instance.public_ip_address, instance.state)
