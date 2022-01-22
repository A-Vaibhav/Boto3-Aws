import boto3

ec2_resource = boto3.resource('ec2')
sns_client = boto3.client('sns')

###### Create Ebs snapshot of instance and email the snapshots id

instances = ec2_resource.instances.all()

snapshots_ids = []

for instance in instances:
    snapshots = ec2_resource.create_snapshot(
        VolumeId = instance.block_device_mappings[0]['Ebs']['VolumeId'],
        TagSpecifications = [
            {
                'ResourceType':'snapshot',
                'Tags': [{'Key':'Name','Value': 'Vai-Snaps'}]
            }
        ]
    )

    snapshots_ids.append(snapshots.snapshot_id)



response = sns_client.publish(
    TopicArn = 'arn:aws:sns:ap-south-1:861390422921:snaps',
    Subject = 'EBS Snapshots', Message = str(snapshots_ids)
)

print(response)
