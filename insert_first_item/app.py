import os
import boto3
import json
import logging
import requests

LOGGER = logging.getLogger()
LOGGER.setLevel(logging.INFO)

def send_response(event, status, reason=None, physical_resource_id=None):
    response_body = {
        'Status': status,  # 'SUCCESS' or 'FAILED'
        'Reason': reason or 'See details in CloudWatch logs',
        'PhysicalResourceId': physical_resource_id or 'MyCustomResource',
        'StackId': event['StackId'],
        'RequestId': event['RequestId'],
        'LogicalResourceId': event['LogicalResourceId'],
        'Data': {}
    }
    
    response_url = event['ResponseURL']
    headers = {'Content-Type': ''}
    
    # Response to CloudFormation
    response = requests.put(response_url, data=json.dumps(response_body), headers=headers)
    return response

def lambda_handler(event, context):
    table_name = os.environ.get('DYNAMODB_TABLE_NAME')
    dynamodb = boto3.client('dynamodb')
    
    try:
        # Insert item into DynamoDB
        response = dynamodb.put_item(
            TableName=table_name,
            Item={
                'PageId': {
                    'S': '1'
                }
            }
        )        
        
        # Log the response from DynamoDB
        LOGGER.info(f"Added Item: Page_Id: 1 to {table_name}")
        LOGGER.info(f"DynamoDB response: {json.dumps(response, indent=2)}")
        
        # Send a success response back to CloudFormation
        send_response(event, 'SUCCESS')
        
        return {
            'message': f"Added Item: Page_Id: 1 to {table_name}",
            'response': json.dumps(response, indent=2)
        }

    except Exception as e:
        # Log the error and send a failure response to CloudFormation
        LOGGER.error(f"Error occurred: {str(e)}")
        send_response(event, 'FAILED', reason=str(e))
        raise e
