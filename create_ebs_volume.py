import boto3

region = 'ap-south-1'

ec2_client = boto3.client('ec2',region_name=region)
ec2_Resources = boto3.resource('ec2',region_name=region)


new_volume = ec2_Resources.create_volume(
    AvailabilityZone = f'{region}c',
    Size = 10,
    VolumeType ='gp2',
    TagSpecifications=[
        {
            'ResourceType':'volume',
            'Tags':[
                {
                    'Key':'Name',
                    'Value':'Vaibhav-ebs-boto3'
                }
            ]
        }
    ]
)

# print(new_volume)     # with client it is dictionary file and you have to use below code to print
# print(f'Created volume Id : {new_volume["VolumeId"]} {new_volume["Tags"][0]["Value"]}')

# print(new_volume.tags)     # with resource it is object file you have to access every attribute with '.'
print(f'Created volume Id : {new_volume.volume_id} Tags : {new_volume.tags[0]["Value"]}')