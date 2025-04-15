#!/usr/bin/env python3
import sys
import os
import requests
import boto3

if len(sys.argv) != 4:
    print("Usage: {} <file_url> <bucket_name> <expiration_in_seconds>".format(sys.argv[0]))
    sys.exit(1)

file_url = sys.argv[1]
bucket_name = sys.argv[2]
expiration = int(sys.argv[3])

filename = os.path.basename(file_url)
if not filename:
    filename = "downloaded_file.gif"

response = requests.get(file_url)
response.raise_for_status()
with open(filename, "wb") as f:
    f.write(response.content)

s3 = boto3.client("s3", region_name="us-east-1")
s3.upload_file(filename, bucket_name, filename)

url = s3.generate_presigned_url(
    ClientMethod='get_object',
    Params={'Bucket': bucket_name, 'Key': filename},
    ExpiresIn=expiration
)
print("Presigned URL:")
print(url)
