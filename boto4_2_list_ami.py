import boto3

region = "ap-south-1"
ec2_resource = boto3.resource('ec2', region_name = region)


###### list all the AMI including the public AMI

images = ec2_resource.images.all()

for image in images:
    print(f'AMI {image.id}: {image.name}')


