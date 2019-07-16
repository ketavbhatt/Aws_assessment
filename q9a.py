import boto3

# Get the service resource.
dynamodb = boto3.setup_default_session(region_name='us-east-1')
dynamodb = boto3.resource('dynamodb')

# Create the DynamoDB table.
table = dynamodb.create_table(
    TableName='ketav-Games',
    KeySchema=[
        {
            'AttributeName': 'gid',
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'rating',
            'KeyType': 'RANGE'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'gid',
            'AttributeType': 'N'
        },
        {
            'AttributeName': 'rating',
            'AttributeType': 'N'
        },
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }
)

# Wait until the table exists.
table.meta.client.get_waiter('table_exists').wait(TableName='ketav-Games')

# Print out some data about the table.
print(table.item_count)
