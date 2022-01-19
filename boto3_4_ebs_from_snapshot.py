import boto3

region = "ap-south-1"
ec2_resource = boto3.resource('ec2', region_name = region)

###### create an EBS volume from a Snapshot
snapshot_id = 'snap-0bb9dcd1a0b442fbb'

new_volume = ec2_resource.create_volume(
    AvailabilityZone = 'ap-south-1a',
    SnapshotId = snapshot_id,
    VolumeType = 'gp2',
    TagSpecifications = [
        {
            'ResourceType':'volume',
            'Tags':[{'Key':'Name','Value':'Vai-Ebs'}]
        }
    ]
)

print(f'Created volume {new_volume.id} from snapshot {snapshot_id}')