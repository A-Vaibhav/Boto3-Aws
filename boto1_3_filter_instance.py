import boto3

region = 'ap-south-1'
ec2_resource = boto3.resource('ec2',region_name=region)


###### Filter Instance by Id

# instance_id = "i-0235e6f5e25b5d70b"
# instances = ec2_resource.instances.filter(
#     InstanceIds=[instance_id]
# )


###### Filter Instance by type 

# instance_type = 't2.micro'
# instances = ec2_resource.instances.filter(
#     Filters=[{'Name':'instance-type','Values':[instance_type]}]
# )


###### Filter Instance by  Tag

# instance_name = "My-Server" 
# instances = ec2_resource.instances.filter(
#     Filters=[{'Name':'tag:Name','Values':[instance_name]}]
# )
# # print(f'Instance Name: {instance.tags[0]["Value"]} ({instance.platform_details})')


###### Filter Instance by state

state_name = 'stopped'
instances = ec2_resource.instances.filter(
    Filters=[{'Name': 'instance-state-name','Values': [state_name]}]
)

print(f'Following are the Instances with {state_name} state:')

for instance in instances:
    print(f'Instance ID: {instance.id} ({instance.platform_details})')
    


