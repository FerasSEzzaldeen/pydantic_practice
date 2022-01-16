from src.transformers.employee_transformer import transform
import boto3
from os import getenv
import json


s3 = boto3.resource('s3', endpoint_url=getenv('AWS_ENDPOINT_URL'))
bucket = s3.Bucket('feras-bucket')

sqs_resource = boto3.resource('sqs', endpoint_url=getenv('AWS_ENDPOINT_URL'))
sqs_client = boto3.client("sqs", endpoint_url=getenv('AWS_ENDPOINT_URL'))
queue = sqs_resource.get_queue_by_name(QueueName="sqs-queue")


response = {"Messages": None}

file = open("data/output.json", "a")

while 'Messages' in response.keys():
    response = sqs_client.receive_message(
        QueueUrl=queue.url,
        MaxNumberOfMessages=1,
    )

    if response.get("Messages") is None:
        continue

    line = response['Messages'][0]['Body']
    new_line = transform(json.loads(line))
    file.write(f"{json.dumps(new_line)}\n")
    deleted_messages = sqs_client.delete_message(
        QueueUrl=queue.url,
        ReceiptHandle=response['Messages'][0]['ReceiptHandle']
    )

file.close()
bucket.upload_file('data/output.json', 'final')
