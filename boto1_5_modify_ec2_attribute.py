import boto3 

region = 'ap-south-1'
ec2_resource = boto3.resource('ec2', region_name = region)

##### changing EC2 instance type of specified Instance

instance_id = 'i-07a98f436a479777b'

instance = ec2_resource.Instance(instance_id)
instance.stop()
instance.wait_until_stopped()

instance.modify_attribute(InstanceType={'Value':'t2.small'})
