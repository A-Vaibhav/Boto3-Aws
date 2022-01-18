import boto3

region = 'ap-south-1'
ec2_resource = boto3.resource('ec2', region_name = region)

###### List the Ebs volumes attached to specific Ec2 instance

# instance_id = 'i-057afa78d84178c05'  # updated the id 

# instance_details = ec2_resource.Instance(instance_id)

# device_mapped = instance_details.block_device_mappings

# print(f'Volumes Attached to {instance_id} :')
# for device in device_mapped:
#     print(f"- {device['Ebs']['VolumeId']} attached as {device['DeviceName']}")



###### List all the EBS Volumes 
# volumes = ec2_resource.volumes.all()

# for volume in volumes:
#     print(volume)



###### Find EBS Volume with Tag Name and its in use or not

for volume in ec2_resource.volumes.filter(
    Filters = [{'Name':'tag:Name','Values':['vai-ebs']}]
):
    print(f'Volume {volume.id} {volume.size} GB {volume.state}')


