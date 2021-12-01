import json
import boto3
import sys
import logging

# logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

VERSION = 1.0

s3 = boto3.client('s3')

def lambda_handler(event, context):
    bucket = 'myjason-cr'
    key = 'sample_json.json'
    
    response = s3.get_object(Bucket = bucket, Key = key)
    content = response['Body']
    jsonObject = json.loads(content.read())
    print(jsonObject)
    return jsonObject