import boto3


# client = boto3.client('s3')
# response = client.list_buckets()
# print(response)

aws_resource = boto3.resource('s3')
bucket = aws_resource.Bucket('nvson5')
response = bucket.create(
    ACL='private',
    CreateBucketConfiguration={
        'LocationConstraint': 'ap-southeast-1'
    },
)

print(response)
