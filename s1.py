import boto3
import os
import json
import uuid

s3 = boto3.client('s3')
BUCKET_NAME = 'xml-upload-bucket-example'

def lambda_handler(event, context):
    # Optional: Extract filename or generate a unique one
    filename = event.get('queryStringParameters', {}).get('filename') or f"{uuid.uuid4()}.xml"

    # Generate presigned URL
    presigned_url = s3.generate_presigned_url(
                'put_object',
                        Params={'Bucket': BUCKET_NAME, 'Key': filename, 'ContentType': 'application/xml'},
                                ExpiresIn=300  # 5 minutes
                                    )

    return {
                'statusCode': 200,
                        'headers': {'Content-Type': 'application/json'},
                                'body': json.dumps({'url': presigned_url, 'key': filename})
                                    }

