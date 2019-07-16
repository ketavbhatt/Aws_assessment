import json
import boto3



def lambda_handler(event, context):
    # To get s3 resource
    s3 = boto3.client('s3')

    # Destination bucket
    dest_bucket="ketav-destinationbucket"

    # Getting key of the object
    key=event["Records"][0]["s3"]["object"]["key"]

    # Getting Source object bucket
    bucket=event["Records"][0]["s3"]["bucket"]["name"]

    # Coping object from source to destination bucket
    s3.copy_object(Bucket=dest_bucket,Key=key,CopySource={'Bucket':bucket,'Key':key})

    
    return {
        'statusCode': 200,
        'body': event["Records"][0]["s3"]["object"]["key"]
    }
