import json
import os
import logging
from botocore.vendored import requests

# Initializing a logger and settign it to INFO
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Reading environment variables and generating a Telegram Bot API URL
BOT_ID = os.environ['BOT_ID']
CHAT_ID = os.environ['CHAT_ID']
API_ENDPOINT = "https://api.telegram.org/bot{}/sendMessage".format(BOT_ID)

# Helper function to prettify the message if it's in JSON
def process_message(input):
    try:
        # Loading JSON into a string
        raw_json = json.loads(input)
        # Outputing as JSON with indents
        output = json.dumps(raw_json, indent=4)
    except:
        output = input
    return output

# Main Lambda handler
def lambda_handler(event, context):
    # logging the event for debugging
    logger.info("event=")
    logger.info(json.dumps(event))

    # Basic exception handling. If anything goes wrong, logging the exception    
    try:
        # Reading the message "Message" field from the SNS message
        message = process_message(event['Records'][0]['Sns']['Message'])

        # Payload to be set via POST method to Telegram Bot API
        payload = {
            "text": message.encode("utf8"),
            "chat_id": CHAT_ID
        }

        # Posting the payload to Telegram Bot API
        requests.post(API_ENDPOINT, payload)

    except Exception as e:
        raise e