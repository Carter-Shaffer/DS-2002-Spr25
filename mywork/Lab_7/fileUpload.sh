#!/bin/bash

if [ "$#" -ne 3 ]; then
    echo "Usage: $0 <local_file> <bucket_name> <expiration_in_seconds>"
    exit 1
fi

LOCAL_FILE=$1
BUCKET_NAME=$2
EXPIRES_IN=$3

echo "Uploading ${LOCAL_FILE} to s3://${BUCKET_NAME}/..."
aws s3 cp "${LOCAL_FILE}" s3://"${BUCKET_NAME}"/

echo "Generating presigned URL (valid for ${EXPIRES_IN} seconds)..."
PRESIGNED_URL=$(aws s3 presign --expires-in "${EXPIRES_IN}" s3://"${BUCKET_NAME}"/$(basename "${LOCAL_FILE}"))

echo "Presigned URL:"
echo "${PRESIGNED_URL}"
