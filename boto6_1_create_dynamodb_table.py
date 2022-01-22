import boto3

dynamo = boto3.resource('dynamodb')

table = dynamo.create_table(
    TableName = 'Json_data',
    KeySchema=[
        {
            'AttributeName':'emp_id',
            'KeyType':'HASH'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'emp_id',
            'AttributeType': 'N'
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }
)

print(f'Table status : {table.table_status} "{table.table_name}" Table ')
table.wait_until_exists()

print(f'Table status : CREATED "{table.table_name}" Table')