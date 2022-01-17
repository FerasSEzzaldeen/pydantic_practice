import json
import uuid
from os import getenv

import boto3
import redis
from src.transformers.employee_transformer import transform

redis_client = redis.StrictRedis(host=getenv('REDIS_HOST'), port=getenv('REDIS_PORT'))
s3 = boto3.resource('s3', endpoint_url=getenv('AWS_ENDPOINT_URL'))
bucket = s3.Bucket('feras-bucket')

sqs_resource = boto3.resource('sqs', endpoint_url=getenv('AWS_ENDPOINT_URL'))
queue = sqs_resource.get_queue_by_name(QueueName="sqs-queue")
ids = []
while (int(queue.attributes['ApproximateNumberOfMessages']) > 0
       or int(queue.attributes['ApproximateNumberOfMessagesNotVisible'])) > 0:
    response = queue.receive_messages()
    line = response[0].body
    new_line = transform(json.loads(line))
    id = uuid.uuid4().int
    redis_client.set(id, json.dumps(new_line))
    ids.append(id)
    response[0].delete()


file = open("data/output.json", "a")
for x in ids:
    file.write(f"{redis_client.get(x)}\n")

file.close()
bucket.upload_file('data/output.json', 'final')
redis_client.flushdb()
