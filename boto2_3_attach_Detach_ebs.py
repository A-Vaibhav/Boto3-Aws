import boto3

region = 'ap-south-1'
ec2_resource = boto3.resource('ec2', region_name = region)
instance_id = 'i-097ebf9df4e97832d'


###### Attach Ebs volume to ec2 using instance id

# volume = ec2_resource.Volume('vol-06bedb867bd44ad61')

# print(f'Volume {volume.id} Status : {volume.state}')

# volume.attach_to_instance(
#     Device='/dev/sdh',
#     InstanceId=instance_id
# )

# print(f'Volume {volume.id} Status : {volume.state}')


###### Detach EBS Volume from EC2 Instance

volume = ec2_resource.Volume('vol-06bedb867bd44ad61')
ec2_client = boto3.client('ec2', region_name = region)
print(f'Volume {volume.id} status -> {volume.state}')

# print(volume.attachments)

volume.detach_from_instance(
    Device=volume.attachments[0]['Device'],
    InstanceId=instance_id
)

waiter = ec2_client.get_waiter('volume_available')
waiter.wait(VolumeIds=[volume.id])
print(f'Volume {volume.id} status -> {volume.state}')

