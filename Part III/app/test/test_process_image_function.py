import os
from PIL import Image

event: dict = {
    "Records": [
        {
            "s3": {
                "bucket": {"name": "test-photos-upload"},
                "object": {"key": "uploads/Manggo_700x368.jpg"},
            }
        }
    ],
}


# Check if process_image_function returns the correct result if it succeeds
def test_process_image_succeeded(s3_client, s3_create_buckets, mock_upload_file):
    from functions.process_image_function import handler

    # Retrieve and process test photo from S3
    result: dict = handler(event=event, context="")

    # Check if the function returns the correct result
    assert result["status"] == "SUCCEEDED"
    assert (
        result["presigned_url"].startswith(
            "https://test-photos-processed.s3.amazonaws.com/processed/Manggo_700x368.jpg"
        )
        == True
    )

    # Check if file is saved in the bucket with the correct key
    response: dict = s3_client.get_object(
        Bucket=os.getenv("S3_PROCESSED_BUCKET"), Key="processed/Manggo_700x368.jpg"
    )
    assert response["ResponseMetadata"]["HTTPStatusCode"] == 200
    assert response["ContentType"] == "image/jpg"

    # Check if file is saved with the correct size
    with Image.open(response["Body"]) as image:
        assert image.size == (200, 105)


# Check if process_image_function fails when there is no bucket
def test_process_image_no_bucket(s3_client):
    from functions.process_image_function import handler

    # Check if the function returns the correct result
    result: dict = handler(event=event, context="")
    assert result["status"] == "FAILED"


# Check if process_image_function fails when there is no file
def test_process_image_no_file(s3_client, s3_create_buckets):
    from functions.process_image_function import handler

    # Check if the function returns the correct result
    result: dict = handler(event=event, context="")
    assert result["status"] == "FAILED"
