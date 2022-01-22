import boto3

ec2_resource = boto3.resource('ec2')
sns_client = boto3.client('sns')

volumes = ec2_resource.volumes.all()

volume_ids = []

for volume in volumes:
    if volume.state != "in-use":
        volume_ids.append(volume.id)


response = sns_client.publish(
    TopicArn = 'arn:aws:sns:ap-south-1:861390422921:snaps',
    Subject = 'Unused Volumes',
    Message = f'Unused volumed : {str(volume_ids)}'
)

print(response)