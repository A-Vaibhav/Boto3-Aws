import boto3

region = 'ap-south-1'
ec2_resource = boto3.resource('ec2',region_name=region)
state = 'terminated'

instances = ec2_resource.instances.filter(
    Filters=[
        {
            'Name': 'instance-state-name',
            'Values': [
                state
            ]
        }
    ]
)

print(f'Instances in {state} state:')

for instance in instances:
    print(f'Instance ID: {instance.id} ({instance.platform_details})')