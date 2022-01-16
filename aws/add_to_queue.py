import boto3
from os import getenv

sqs_resource = boto3.resource('sqs', endpoint_url=getenv('AWS_ENDPOINT_URL'))

queue = sqs_resource.get_queue_by_name(QueueName="sqs-queue")

with open("data/input.json", "r") as data:
    lines = data.readlines()
    for line in lines:
        queue.send_message(
            MessageBody=line)
