def handler(event, context):
    print("SUCCEEDED")
    print(f"Presigned URL: {event["detail"]["responsePayload"]["presigned_url"]}")
