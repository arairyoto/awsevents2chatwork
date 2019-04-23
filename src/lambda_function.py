import os
import requests
from lib.flatten_dict import flatten

# Environment Variables
ENDPOINT = os.getenv('ENDPOINT')
ROOMID = os.getenv('ROOMID')
APIKEY = os.getenv('APIKEY')
FORMAT = os.getenv('FORMAT')

def handler(event, context):
    """
    Function to notify AWS Events via Chatwork
    ・DynamoDB
    ・Amazon Kinesis Data Streams
    ・Amazon S3
    ・Amazon SQS
    ・CloudFront
    ・Amazon SES
    ・Amazon SNS
    """
    # load event records
    records = event['Records']
    # define how to reduce nested keys
    reducer = lambda _, x: _ + '_' + str(x) if _ else str(x)
    for record in records:
        # flatten record
        # record['Sns']['Subject'] -> flatten_record['Sns_Subject']
        flatten_record = flatten(record, reducer)
        # generate body
        body = FORMAT.format(**flatten_record)
        # send to chatwork
        requests.post(
            f'{ENDPOINT}/rooms/{ROOMID}/messages',
            headers={
                'X-ChatWorkToken': APIKEY
            },
            params={
                'body': body
            }
        )
