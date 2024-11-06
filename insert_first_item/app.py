import os
import boto3
import json

def lambda_handler(event, context):
    table_name = os.environ.get('DYNAMODB_TABLE_NAME')
    
    dynamodb = boto3.client('dynamodb')
    
    response = dynamodb.put_item(
        TableName=table_name,
        Item={
            'PageId': {
                'S': '1'
            }
        }
    )    
    
    return {
        'message': f"Added Item: Page_Id: 1 to {table_name}",
        'response': json.dumps(response, indent=2)
    }