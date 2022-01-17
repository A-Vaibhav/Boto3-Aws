import boto3

region = 'ap-south-1'
ec2_Resource = boto3.resource('ec2', region_name = region)

instances = ec2_Resource.instances.all()


for instance in instances:
    print(
    f'''
    Ec2 instance {instance.id} information :
    Instance State : {instance.state['Name']}
    Instance Ami : {instance.image.id}
    Instance Platform : {instance.platform_details}
    Instance type : {instance.instance_type}
    Instance Public Ipv4 : {instance.public_ip_address}
    '''
    )