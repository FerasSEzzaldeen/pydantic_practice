import boto3
from os import getenv

s3 = boto3.resource('s3', endpoint_url=getenv('AWS_ENDPOINT_URL'))
response = s3.create_bucket(
    Bucket="feras-bucket"
)

print("gbgbgb", response)

bucket = s3.Bucket('feras-bucket')
bucket.upload_file('data/input.json', 'done')

bucket.download_file('done', 'data/output.json')

for obj in bucket.objects.all():
    print('hello', obj)

delete_response = bucket.delete_objects(
    Delete={
        'Objects': [
            {
                'Key': 'done',
            },
        ]
    }
)


print(delete_response)

