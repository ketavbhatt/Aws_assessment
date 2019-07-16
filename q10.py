import boto3

from boto3.dynamodb.conditions import Key, Attr

# Get the service resource.
dynamodb = boto3.setup_default_session(region_name='us-east-1')
dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('ketav-Games')

response = table.query(
    KeyConditionExpression=Key('gid').eq(2)
)
items = response['Items']

print("GNAME",end="  ")
print("RATING")


for item in items:
	name = item[u'gname']
	rat = item[u'rating']
	print(name,end="  ")
	print(rat)