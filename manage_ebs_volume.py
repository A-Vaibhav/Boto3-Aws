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
#     print(f'Volume_Id:{volume.volume_id} state:{volume.state}')



###### Find EBS Volume with Tag Name and its in use or not

# for volume in ec2_resource.volumes.filter(
#     Filters = [{'Name':'tag:Name','Values':['vai-ebs']}]
# ):
#     print(f'Volume {volume.id} {volume.size} GB {volume.state}')


###### FInd EBS Volume with volume id

# for volume in ec2_resource.volumes.filter(
#     VolumeIds=[
#         'vol-06bedb867bd44ad61',
#     ]
# ):
#     print(f'Volume {volume.id} ({volume.size} GiB) -> {volume.state}')

###### Delete volume if not in use

# for volume in ec2_resource.volumes.all():
#     if volume.state != 'in-use':
#         volume.delete()
#         print(f"Volume {volume.volume_id} successfully deleted")
#     else:
#         print(f"Can't delete volume : {volume.volume_id}, attaced to Instance : {volume.attachments[0]['InstanceId']}")

