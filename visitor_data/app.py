import json
import uuid
import boto3
from boto3.dynamodb.conditions import Key
from datetime import datetime



def lambda_handler(event, context):
    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.Table("PageVisits2")
    method = event.get('httpMethod')

    if method == 'POST':
        page_id = str(uuid.uuid4())
        current_timestamp = datetime.now().isoformat()

        try:
            item_to_insert = {
                "PageId": page_id,
                "Timestamp": current_timestamp,
                "BrowserType": event.get("headers", {}).get("User-Agent", "Error receiving userAgent data"),
            }
            
            table.put_item(Item=item_to_insert)

            response = table.query(KeyConditionExpression=Key("PageId").eq("1"))
            visitcount = int(response["Items"][0].get("TotalVisits", 0)) if response["Items"] else 0
            visitcount += 1
            
            table.update_item(
                Key={"PageId": "1"},
                UpdateExpression="SET TotalVisits = :new_total",
                ExpressionAttributeValues={":new_total": visitcount},
            )
            
            return {
                'statusCode': 200,
                'body': json.dumps({
                    'message': f'Updated total visits: {visitcount}',
                    'item_inserted': item_to_insert  
                })
            }

        except Exception as e:
            return {
                'statusCode': 500,
                'body': json.dumps({'error': str(e)})
            }

    elif method == 'GET':
        try:
            response = table.query(KeyConditionExpression=Key("PageId").eq("1"))
            visitcount = int(response["Items"][0].get("TotalVisits", 0)) if response["Items"] else 0
            return {
                'statusCode': 200,
                'body': json.dumps({
                    'TotalVisits': visitcount 
                })
            }  

        except Exception as e:
            return {
                'statusCode': 500,
                'body': json.dumps({'error': str(e)})
            }
    else:
        return {
            'statusCode': 200,
            'body': 'Neither POST nor GET'
        }