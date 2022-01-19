from tracemalloc import Snapshot
import boto3

region = 'ap-south-1'
ec2_resource = boto3.resource('ec2',region_name = region)


######  List all the EBS Volume snapshots owned by you and all publicly available snapshots 

# snapshots = ec2_resource.snapshots.all()

# for snapshot in snapshots:
#     print(f'Snapshot {snapshot.id} created for volume {snapshot.volume_id}')


###### List EBS volume snapshots by account id 

sts_client = boto3.client('sts')

our_account_id = sts_client.get_caller_identity()['Account']

snapshots = ec2_resource.snapshots.filter(
    OwnerIds=[our_account_id]
)

for snapshot in snapshots:
    print(f'Snapshot {snapshot.id} created for volume {snapshot.volume_id}')




# print(dir(snapshots))