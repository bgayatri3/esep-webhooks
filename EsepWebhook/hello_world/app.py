import json
import os
import requests

def lambda_handler(event, context):
    # GitHub webhook payload comes in 'body'
    body = event.get("body", "{}")
    if isinstance(body, str):
        try:
            body = json.loads(body)
        except json.JSONDecodeError:
            return {
                "statusCode": 400,
                "body": "Invalid JSON in request body"
            }

    # Extract the issue URL
    issue_url = body.get("issue", {}).get("html_url")

    # Prepare the payload for Slack
    payload_text = f"Issue Created: {issue_url}" if issue_url else "Issue Created: None"
    payload = {"text": payload_text}

    # Send to Slack using environment variable
    slack_url = os.environ.get("SLACK_URL")
    if not slack_url:
        return {
            "statusCode": 500,
            "body": "Slack URL environment variable not set"
        }

    response = requests.post(slack_url, json=payload)
    
    return {
        "statusCode": response.status_code,
        "body": response.text,
        "headers": {
            "Content-Type": "text/plain"
        }
    }
