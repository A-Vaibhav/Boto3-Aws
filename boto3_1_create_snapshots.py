import boto3

region = 'ap-south-1'
ec2_resource = boto3.resource('ec2', region_name = region)

###### Create snapshot using Ebs volume
volume_id = 'vol-0f860c20176d0ed6d'

snapshot = ec2_resource.create_snapshot(
    VolumeId = volume_id,
    TagSpecifications = [
        {
            'ResourceType':'snapshot',
            'Tags':[{'Key':'Name','Value':'Vai-snapshot'}]
        }
    ]
)
# print(dir(snapshot))
snapshot.wait_until_completed()

print(f"Snapshot {snapshot.id} created for volume {volume_id}")