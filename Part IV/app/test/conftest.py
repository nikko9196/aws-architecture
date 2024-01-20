import os
import pytest
import boto3
from unittest import mock
from moto import mock_s3


@pytest.fixture(autouse=True)
def aws_environment():
    """Mock Environment Variables for testing."""
    with mock.patch.dict(
        os.environ,
        {
            "S3_UPLOAD_BUCKET": "test-photos-upload",
            "S3_PROCESSED_BUCKET": "test-photos-processed",
            "EVENTBRIDGE_NAME": "test-image-processing-bus",
        },
    ):
        yield


@pytest.fixture
def s3_client():
    """Mock AWS S3 client using moto."""
    with mock_s3():
        s3 = boto3.client("s3")
        yield s3
        s3 = None


@pytest.fixture
def s3_create_buckets(s3_client):
    """Create mock AWS S3 bucket for storing data."""
    s3_client.create_bucket(Bucket=os.getenv("S3_UPLOAD_BUCKET"))
    s3_client.create_bucket(Bucket=os.getenv("S3_PROCESSED_BUCKET"))
    yield
    s3_client.delete_bucket(Bucket=os.getenv("S3_UPLOAD_BUCKET"))
    s3_client.delete_bucket(Bucket=os.getenv("S3_PROCESSED_BUCKET"))


@pytest.fixture
def mock_upload_file(s3_client, s3_create_buckets):
    """Upload test file to AWS S3"""
    s3_client.upload_file(
        Filename="Manggo_700x368.jpg",
        Bucket=os.getenv("S3_UPLOAD_BUCKET"),
        Key="uploads/Manggo_700x368.jpg",
        ExtraArgs={"ContentType": "image/jpg"},
    )

    yield
    s3_resource = boto3.resource("s3")
    upload_bucket = s3_resource.Bucket(os.getenv("S3_UPLOAD_BUCKET"))
    upload_bucket.objects.delete()
    process_bucket = s3_resource.Bucket(os.getenv("S3_PROCESSED_BUCKET"))
    process_bucket.objects.delete()
