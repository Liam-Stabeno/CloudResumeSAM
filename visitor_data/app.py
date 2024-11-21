import json
import uuid
import boto3
import os
from boto3.dynamodb.conditions import Key
from datetime import datetime


def lambda_handler(event, context):
    tableName = os.environ['DYNAMODB_TABLE_NAME']
    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.Table(tableName)

    method = event["requestContext"]["http"]["method"]
    
    if method == 'GET':
        # Generate a unique page ID and timestamp
        page_id = str(uuid.uuid4())
        current_timestamp = datetime.now().isoformat()

        try:
            # Query the table to get the current visit count for PageId '1'
            response = table.query(KeyConditionExpression=Key("PageId").eq("1"))
            visitcount = int(response["Items"][0].get("TotalVisits", 0)) if response["Items"] else 0
            visitcount += 1

            # Insert a new record with the current page visit data (including user-agent and IP)
            item_to_insert = {
                "PageId": page_id,
                "Timestamp": current_timestamp,
                "BrowserType": event.get("headers", {}).get("user-agent", "Error receiving userAgent data"),
                "IP": event.get("requestContext", {}).get("http", {}).get("sourceIp", "Error receiving IP data")
            }

            table.put_item(Item=item_to_insert)

            # Update the total visit count for PageId "1"
            table.update_item(
                Key={"PageId": "1"},
                UpdateExpression="SET TotalVisits = :new_total",
                ExpressionAttributeValues={":new_total": visitcount},
            )

            # Return the updated visit count
            return {
                'statusCode': 200,
                'body': json.dumps({
                    'TotalVisits': visitcount,
                    'item_inserted': item_to_insert
                })
            }

        except Exception as e:
            return {
                'statusCode': 500,
                'body': json.dumps({'error': str(e)})
            }
    else:
        # Return the event if the method is neither GET nor POST
        return {
            'statusCode': 200,
            'body': json.dumps(event)
        }
