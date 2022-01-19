import boto3

region = 'ap-south-1'
ec2_resource = boto3.resource('ec2',region)
instances = ec2_resource.instances.all()


#####  Start stopped Servers :
# for instance in instances:
#     if instance.state['Name'] == 'stopped':
#         instance.start()
#         print(f'Started {instance.id} {instance.platform_details} server')


#####  Stop running Servers :
# for instance in instances:
#     if instance.state['Name'] == 'running':
#         instance.stop()
#         print(f'Stopped {instance.id} {instance.platform_details} server')


##### Terminate specific Server with Id :
instance_id = 'i-03acd8efcdfc7b95d'
instance = ec2_resource.Instance(instance_id)

instance.terminate()

print(f'Terminating EC2 instance: {instance.id}')
instance.wait_until_terminated()
print(f'EC2 instance {instance.id} has been terminated')
