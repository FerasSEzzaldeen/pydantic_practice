import boto3
from os import getenv

sqs_resource = boto3.resource('sqs', endpoint_url=getenv('AWS_ENDPOINT_URL'))
# sqs_client = boto3.client("sqs", endpoint_url=getenv('AWS_ENDPOINT_URL'))


queue = sqs_resource.get_queue_by_name(QueueName="sqs-queue")

with open("data/input.json", "r") as data:
    lines = data.readlines()
    for line in lines:
        print(line)
        queue.send_message(
            MessageBody=line)

print(queue.attributes)

# response = queue.receive_message(
#         MaxNumberOfMessages=1,
#         WaitTimeSeconds=10,
#     )
# print(response)
# messages = queue.receive_message(AttributeNames=['All'])

# # for message in messages :
# #     print("vvv",message)


# while messages :
#     print("nvvvd",messages)
#     messages = queue.receive_messages(AttributeNames=['All'])
#     print('hello',queue.attributes)
