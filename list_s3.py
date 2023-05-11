import boto3

aws_access_key_id = 'AKIASP2TPHJSWIKYTTCO'
aws_secret_access_key = 'NpPIch3GOQHK7uPmGpRk5eAYglO0VfQX3pF31hyY'
output = json
region = us-east-2

# Create an S3 client with your credentials
s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

# Call the list_buckets method to get a list of all S3 buckets
response = s3.list_buckets()

# Print the name of each bucket
for bucket in response['Buckets']:
    print(bucket['Name'])
