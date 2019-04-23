# Description
Serverless application that sends AWS Events to Chatwork in format as you like.
Following AWS Events are able to be handled in this application.
- DynamoDB
- Amazon Kinesis Data Streams
- Amazon S3
- Amazon SQS
- CloudFront
- Amazon SES
- Amazon SNS

# How to use
As FORMAT variable, specify the format of the content you want to send to chatwork.
In the format, you can use variables the names of which are AWS Event keys combined with "_"(underscore).

# Example
## SNS Topic
### Event (SNS Event)
```
{
  "Records": [
    {
      "EventVersion": "1.0",
      "EventSubscriptionArn": eventsubscriptionarn,
      "EventSource": "aws:sns",
      "Sns": {
        "SignatureVersion": "1",
        "Timestamp": "1970-01-01T00:00:00.000Z",
        "Signature": "EXAMPLE",
        "SigningCertUrl": "EXAMPLE",
        "MessageId": "95df01b4-ee98-5cb9-9903-4c221d41eb5e",
        "Message": "Hello from SNS!",
        "MessageAttributes": {
          "Test": {
            "Type": "String",
            "Value": "TestString"
          },
          "TestBinary": {
            "Type": "Binary",
            "Value": "TestBinary"
          }
        },
        "Type": "Notification",
        "UnsubscribeUrl": "EXAMPLE",
        "TopicArn": topicarn,
        "Subject": "TestInvoke"
      }
    }
  ]
}
```
### Format
```
FORMAT = [info][title]{EventSubscriptionArn}[/title]Message:{Sns_Message}[/info]
```
### Result
```
===============
ⓘ eventsubscriptionarn
===============
Message:Hello from SNS!
```
# License
MIT License (MIT)
This software is released under the MIT License, see LICENSE.txt.