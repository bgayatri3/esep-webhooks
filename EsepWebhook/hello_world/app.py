import json

# import requests


def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """

    # try:
    #     ip = requests.get("http://checkip.amazonaws.com/")
    # except requests.RequestException as e:
    #     # Send some context about this error to Lambda Logs
    #     print(e)

    #     raise e

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
            # "location": ip.text.replace("\n", "")
        }),
    }

##################################################
# import json

# def lambda_handler(event, context):
#     """
#     AWS Lambda handler for GitHub Webhook events.
#     """

#     print("Received event:", json.dumps(event))

#     # Parse body
#     try:
#         body = json.loads(event.get('body', '{}'))
#     except json.JSONDecodeError:
#         return {
#             "statusCode": 400,
#             "body": json.dumps({"message": "Invalid JSON"})
#         }

#     # Get GitHub event type from headers
#     github_event = event.get('headers', {}).get('X-GitHub-Event', 'unknown')
#     print(f"GitHub event type: {github_event}")

#     # Example: handle push event
#     if github_event == "push":
#         repo = body.get("repository", {}).get("full_name", "unknown")
#         pusher = body.get("pusher", {}).get("name", "unknown")
#         print(f"Push to {repo} by {pusher}")

#     return {
#         "statusCode": 200,
#         "body": json.dumps({"message": "Received", "event": github_event})
#     }
##################################################
