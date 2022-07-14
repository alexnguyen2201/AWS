# S3 

##  Cài đặt AWS CLI ver 2 vào /usr/local/bin/aws
https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html

- Cài vào `/usr/local/bin/`thì kết nối aws được
- Cài vào homebrew bằng pip (version 1) không kết nối aws được

## AWS configure
```bash
aws configure
AWS Access Key ID [****************VEMB]:
AWS Secret Key [****************VEMB]:
Default region name [None]: ap-southeast-1
Default output format [None]: json
```

Kiểm tra kết nối:
https://aws.amazon.com/premiumsupport/knowledge-center/s3-access-key-error/

```bash
aws sts get-caller-identity
```

## Tạo bucket
```python
import boto3

aws_resource = boto3.resource('s3')
bucket = aws_resource.Bucket('nvson5')
response = bucket.create(
    ACL='public-read',
    CreateBucketConfiguration={
        'LocationConstraint': 'ap-southeast-1'
    },
)

print(response)
```
## Xem danh sách bucket
```python
import boto3
client = boto3.client('s3')
response = client.list_buckets()
print(response)
```