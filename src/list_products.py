import boto3
import json

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('ButcheryProducts')

def lambda_handler(event, context):
    response = table.scan()
    return {
        'statusCode': 200,
        'body': json.dumps(response['Items'])
    }
