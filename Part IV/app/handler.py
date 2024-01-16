import json
import boto3
import os
import sys
import uuid
from urllib.parse import unquote_plus

import pydantic as py

from PIL import Image
import PIL.Image

# Environment variables
S3_PROCESSED_BUCKET = os.getenv("S3_PROCESSED_BUCKET")

# Clients
s3_client = boto3.client("s3")


def resize_image(image_path, resized_path, max_width=200):
    with Image.open(image_path) as image:
        print(f"original image size {image.size}")

        if image.width >= max_width:
            ratio = max_width / image.width
            new_height = int(image.height * ratio)
            resized_image = image.resize((max_width, new_height))

            resized_image.save(resized_path)
            print(f"resize image size {resized_image.size}")

        else:
            resized_image = image.resize((image.width, image.height))
            resized_image.save(resized_path)
            print(f"resize image size {resized_image.size}")


def process_image_function(event, context):
    try:
        for record in event["Records"]:
            bucket_name = record["s3"]["bucket"]["name"]
            original_s3_path = unquote_plus(record["s3"]["object"]["key"])

            print(f"The image name is s3://{bucket_name}/{original_s3_path}")
            destination_s3_path = original_s3_path.replace("uploads", "processed", 1)
            # original = uploads/kitty-cat-kitten-pet-45201.jpg

            # destination = thumbnails/kitty-cat-kitten-pet-45201.jpg
            print(
                f"The resize name is s3://{S3_PROCESSED_BUCKET}/{destination_s3_path}"
            )

            tmpkey = original_s3_path.replace("/", "")
            # adding uuid4 to make sure we process an unique object locally to Lambda
            local_download_path = "/tmp/{}{}".format(uuid.uuid4(), tmpkey)
            print(f"The local image name is {local_download_path}")
            local_upload_path = "/tmp/resized-{}".format(tmpkey)
            print(f"The local resize name is {local_upload_path}")

            s3_client.download_file(bucket_name, original_s3_path, local_download_path)

            resize_image(local_download_path, local_upload_path)

            s3_client.upload_file(
                local_upload_path, S3_PROCESSED_BUCKET, destination_s3_path
            )

            return {"status": "SUCCEEDED"}

    except Exception as e:
        print(f"Error: {e}")
        return {"status": "FAILED"}


def notify_resize_success_function(event, context):
    print("SUCCEED")


def notify_resize_fail_function(event, context):
    print("FAILED")


# def process_image_function(event, context):
#     if event["Success"] == True:
#         response = {
#             "statusCode": 200,
#             "body": json.dumps(event)
#         }
#     # response = {"statusCode": 200, "body": json.dumps(body)}

#         return response
#     else:
#         raise Exception("Some error")

#     # Use this code if you don't use the http event with the LAMBDA-PROXY
#     # integration
#     """
#     return {
#         "message": "Go Serverless v1.0! Your function executed successfully!",
#         "event": event
#     }
#     """
