import json
import uuid
from os import getenv

import boto3
import redis
from src.transformers.employee_transformer import transform

redis_client = redis.Redis(host=getenv('REDIS_HOST'), port=getenv('REDIS_PORT'))
s3 = boto3.resource('s3', endpoint_url=getenv('AWS_ENDPOINT_URL'))
bucket = s3.Bucket('feras-bucket')

sqs_resource = boto3.resource('sqs', endpoint_url=getenv('AWS_ENDPOINT_URL'))
queue = sqs_resource.get_queue_by_name(QueueName="sqs-queue")

while (int(queue.attributes['ApproximateNumberOfMessages'])
       or int(queue.attributes['ApproximateNumberOfMessagesNotVisible'])):
    response = queue.receive_messages()
    line = response[0].body
    new_line = transform(json.loads(line))
    redis_client.set(new_line['emp_id'], json.dumps(new_line))
    response[0].delete()


file = open("data/output.json", "a")
for key in redis_client.keys():
    new_line = redis_client.get(key).decode("utf-8")
    file.write(f"{new_line}\n")
    redis_client.delete(key)

file.close()
bucket.upload_file('data/output.json', 'final')
