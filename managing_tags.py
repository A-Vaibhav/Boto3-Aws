import boto3

region = "ap-south-1"
ec2_resource = boto3.resource('ec2', region_name = region)


##### Add tag to Ec2 Instance with id

# instance_id = 'i-0235e6f5e25b5d70b'

# tags = [{'Key':'Name','Value':'My-Server1'}]
# instance = ec2_resource.Instance(instance_id)
# instance.create_tags(Tags=tags)



##### Add Tags to multiple Ec2 with no Name tag

# tags = [{'Key':'Name','Value':f'My-Server{number}'}]
# instances = ec2_resource.instances.all()

# for instance in instances:
#     if instance.tags == None:
#         instance.create_tags(Tags=tags)
#         print(f"Tag have been created for {instance.id}")



##### Listing all tags of Ec2 Instance 

# instances = ec2_resource.instances.all() 

# for instance in instances:
#     if instance.tags != None:
#         for tag in instance.tags:
#             print(f'For {instance.id} the tags are :')
#             print(f"Tag : {tag['Key']}={tag['Value']}")
#     else:
#         print(f'For {instance.id} there are No tags')
#     print("-"*30)


##### Updating Ec2 instance Tags eg : Server1 --> Dev-Server

instances = ec2_resource.instances.all()

old_tags = [{'Key':'Name','Value':'Dev-Server'}]
new_tags = [{'Key':'Name','Value':'Prod-Server'}]

for instance in instances:
    if instance.tags != None:
        for tags in instance.tags:
            if tags['Value']=='Dev-Server':
                instance.create_tags(Tags=new_tags)
                print(f"Tags for instance Id : {instance.id} have changed to {new_tags[0]['Value']}")
    
    
        
