import boto3

region = "ap-south-1"
ec2_resource = boto3.resource('ec2', region_name = region)
ami_id = 'ami-041d6256ed0f2061c'

instances = ec2_resource.create_instances(
    MinCount = 1,
    MaxCount = 1,
    ImageId = ami_id,
    InstanceType = 't2.micro',
    TagSpecifications=[{'ResourceType': 'instance','Tags': [{'Key': 'Name','Value': 'My-Server'}]}]
    )

for instance in instances:
    print(f'EC2 instance "{instance.id}" has been launched')

    instance.wait_until_running()
    print(f'EC2 instance "{instance.id}" has been started')
