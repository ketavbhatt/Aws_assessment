import boto3
dynamodb = boto3.setup_default_session(region_name='us-east-1')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('ketav-Games')

table.put_item(
   Item={
        'gid': 2,
        'gname': 'TKAM',
        'publisher': 'Harper Collins',
        'rating':9,
        'release_date': '2019-07-15',
        'genres':{'mystery','thriller'}
        }
)

print('Done')