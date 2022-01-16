import boto3
from os import getenv

s3 = boto3.resource('s3', endpoint_url=getenv('AWS_ENDPOINT_URL'))
response = s3.create_bucket(
    Bucket="feras-bucket"
)

sqs_client = boto3.client("sqs", endpoint_url=getenv('AWS_ENDPOINT_URL'))
sqs_client.create_queue(QueueName="sqs-queue")
