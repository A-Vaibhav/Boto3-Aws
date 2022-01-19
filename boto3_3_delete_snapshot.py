import boto3

region = "ap-south-1"
ec2_resource = boto3.resource('ec2', region_name = region)


###### delete snapshot with snapshot id
snapshot_id = 'snap-059a8a220830ccc09'
snapshot = ec2_resource.Snapshot(snapshot_id)

snapshot.delete()

print(f"Snapshot {snapshot_id} has been deleted")

