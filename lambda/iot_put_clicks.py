from __future__ import print_function
import boto3
import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)
dynamo = boto3.resource('dynamodb')


def lambda_handler(event, context):
    logging.info('Received event: ' + json.dumps(event))

    table = dynamo.Table("IoTButtonClicks")

    #attributes = event['placementInfo']['attributes']

    dsn = event['deviceInfo']['deviceId']
    click_type = event['deviceEvent']['buttonClicked']['clickType']
    reportedTime = event['deviceEvent']['buttonClicked']['reportedTime']

    logging.info('Putting item')

    response = table.put_item(
        Item={
            'reportedTime': reportedTime,
            'buttonId': dsn,
            'clickType': click_type
            }
        )
