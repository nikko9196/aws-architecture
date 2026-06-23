import boto3
import os

# Environment variables
S3_UPLOAD_BUCKET = os.getenv("S3_UPLOAD_BUCKET", "restart-nikko-random-photos-upload")

# Clients
s3_client = boto3.client("s3")


def upload_test_photo(path: str, filename: str):
    try:
        test_photo_path = f"{path}{filename}"
        destination_path = f"uploads/{filename}"
        s3_client.upload_file(
            test_photo_path,
            S3_UPLOAD_BUCKET,
            destination_path,
            ExtraArgs={"ContentType": "image/jpg"},
        )
        print("Upload photo successfully")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    upload_test_photo(path="", filename="Manggo_700x700.jpg")
    upload_test_photo(path="", filename="Manggo_700x368.jpg")
