# List the Ebs volumes attached to specific Ec2 instance

import boto3

region = 'ap-south-1'
ec2_resource = boto3.resource('ec2', region_name = region)
instance_id = 'i-0235e6f5e25b5d70b'

instance_details = ec2_resource.Instance(instance_id)

device_mapped = instance_details.block_device_mappings
# print(device_mapped)

print(f'Volumes Attached to {instance_id} :')
for device in device_mapped:
    print(f"- {device['Ebs']['VolumeId']} attached as {device['DeviceName']}")
