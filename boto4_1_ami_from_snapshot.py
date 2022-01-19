import boto3

region = "ap-south-1"
ec2_resource = boto3.resource('ec2', region_name = region)

###### create an EBS volume from a Snapshot
snapshot_id = 'snap-0bb9dcd1a0b442fbb'

image = ec2_resource.register_image(
    BlockDeviceMappings = [
        {
            'DeviceName':'/dev/sda1',
            'Ebs':{
                'DeleteOnTermination':True,
                'SnapshotId':snapshot_id,
                'VolumeSize':20,
                'VolumeType':'gp2'
            }
        }
    ],
    Description='Ami from snapshot',
    Name = 'Vai-Ami',
    RootDeviceName = '/dev/sda1',
    VirtualizationType = 'hvm'
)
print(image)


