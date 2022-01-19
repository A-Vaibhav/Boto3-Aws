import boto3

region = "ap-south-1"
ec2_resource = boto3.resource('ec2', region_name = region)


###### Delete AMI using AMI id

ami_id = 'ami-0b13bca6ba67ecb85'

image = ec2_resource.Image(ami_id)

image.deregister()

print(f'{ami_id} successfully Deregistered')