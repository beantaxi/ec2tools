from ec2tools import allThe 

if __name__ == '__main__':
    data = allThe.SecurityGroups()    
    for row in data:
        print('{:20}{:13}{}'.format(row.group_name, row.group_id, row.description))
