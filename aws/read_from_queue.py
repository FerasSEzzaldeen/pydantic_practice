import json
from os import getenv

import boto3
from src.transformers.employee_transformer import transform

s3 = boto3.resource('s3', endpoint_url=getenv('AWS_ENDPOINT_URL'))
bucket = s3.Bucket('feras-bucket')

sqs_resource = boto3.resource('sqs', endpoint_url=getenv('AWS_ENDPOINT_URL'))
queue = sqs_resource.get_queue_by_name(QueueName="sqs-queue")

file = open("data/output.json", "a")

while (int(queue.attributes['ApproximateNumberOfMessages'])
       or int(queue.attributes['ApproximateNumberOfMessagesNotVisible'])):
    response = queue.receive_messages()
    line = response[0].body
    new_line = transform(json.loads(line))
    file.write(f"{json.dumps(new_line)}\n")
    response[0].delete()


file.close()
bucket.upload_file('data/output.json', 'final')
