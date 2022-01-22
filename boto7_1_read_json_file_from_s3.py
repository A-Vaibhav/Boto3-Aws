import boto3
import json

s3_resource = boto3.resource('s3')

buckets = s3_resource.buckets.all()

for bucket in buckets:
    if bucket.name == 'vai-bucket':
        for object in bucket.objects.all():
            if object.key[-4:] == 'json':
               data = object.get()
               real_data = data['Body'].read()  # in string format
               jsondict = json.loads(real_data) # converts in dictionary format


for key,value in jsondict.items():
    print(f'{key}: {value}')
