import boto3
from os import getenv

s3 = boto3.resource('s3', endpoint_url=getenv('AWS_ENDPOINT_URL'))
bucket = s3.Bucket('feras-bucket')
bucket.download_file('final', 'data/check.json')
