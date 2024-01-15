import json


def process_image_function(event, context):
    if event["Success"] == True:
        response = {
            "statusCode": 200,
            "body": json.dumps(event)
        }
    # response = {"statusCode": 200, "body": json.dumps(body)}

        return response
    else:
        raise Exception("Some error")

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """
