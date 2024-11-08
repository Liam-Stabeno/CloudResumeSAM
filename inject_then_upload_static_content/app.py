import boto3
import json
import os
import requests
import mimetypes
from botocore.exceptions import ClientError

s3_client = boto3.client('s3')

def send_response(event, context, status, message):
    """Send response back to CloudFormation"""
    response_url = event['ResponseURL']
    response_body = {
        'Status': status,
        'Reason': message,
        'PhysicalResourceId': context.log_stream_name,
        'StackId': event['StackId'],
        'RequestId': event['RequestId'],
        'LogicalResourceId': event['LogicalResourceId'],
        'Data': {}
    }

    json_response = json.dumps(response_body)
    headers = {'content-type': '', 'content-length': str(len(json_response))}
    
    try:
        response = requests.put(response_url, data=json_response, headers=headers, timeout=15)
        print(f"CloudFormation response sent with status: {status}")
    except requests.RequestException as e:
        print(f"Failed to send CloudFormation response: {e}")

def lambda_handler(event, context):
    try:
        print("Event received:", json.dumps(event, indent=2))  # Log the full event for inspection
        
        # Extract properties from event (CloudFormation provides these)
        bucketname = event['ResourceProperties']['BUCKET_NAME']
        api_endpoint = event['ResourceProperties']['API_ENDPOINT']
        
        files = {
            'index.html': './static/index.html',
            'styles.css': './static/styles.css',
            'favicon.ico': './static/favicon.ico',
        }
        
        # Upload static files to S3
        
        for file_name, file_path in files.items():
            try:
                
                content_type, _ = mimetypes.guess_type(file_path)    # You must implement mimetypes, as S3 does not automatically assign them when uploading in this way
                if not content_type:
                    content_type = 'application/octet-stream'
                    
                print(f"Uploading {file_name} from {file_path} to bucket {bucketname} with ContentType {content_type}")
                
                print(f"Uploading {file_name} from {file_path} to bucket {bucketname}")
                with open(file_path, 'rb') as file_data:
                    s3_client.upload_fileobj(
                        file_data,
                        bucketname,
                        file_name,
                        ExtraArgs={'ContentType': content_type}
                    )
                    
                    print(f"Uploaded {file_name} to {bucketname} with ContentType {content_type}")
                    
            except ClientError as e:
                print(f"Error uploading {file_name}: {e}")
                send_response(event, context, 'FAILED', f"Error uploading {file_name}: {e}")
                raise
        
        # Update index.html with the injected API endpoint
        try:
            with open(files['index.html'], 'r', encoding='utf-8') as file:
                content = file.read()

            content = content.replace('${ApiUrl}', api_endpoint)
            
            s3_client.put_object(
                Bucket=bucketname,
                Key='index.html',
                Body=content,
                ContentType='text/html'
            )
            print(f"Updated index.html with API endpoint: {api_endpoint}")
            
        except ClientError as e:
            print(f"Error updating index.html: {e}")
            send_response(event, context, 'FAILED', f"Error updating index.html: {e}")
            raise
        
        # Send success response to CloudFormation
        send_response(event, context, 'SUCCESS', "Static content uploaded successfully")
    
    except Exception as e:
        print(f"General error in lambda_handler: {e}")
        send_response(event, context, 'FAILED', str(e))
        raise
