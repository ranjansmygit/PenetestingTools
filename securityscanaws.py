# Python script that uses the AWS Security Hub API to run an automated security scan for all of your AWS services and sends the output to an email address
import boto3
from botocore.exceptions import ClientError

# Set up the client for Security Hub
security_hub = boto3.client('securityhub')

# Run the scan
response = security_hub.batch_enable_standards(StandardsSubscriptionRequests=[{'StandardArn': 'arn:aws:securityhub:us-west-2::standard/CISAWSFoundations'}])

# Send the output via email
def send_email(recipient, body):
    SENDER = "sender@example.com"
    AWS_REGION = "us-west-2"
    SUBJECT = "AWS Security Scan Results"
    CHARSET = "UTF-8"
    client = boto3.client('ses', region_name=AWS_REGION)
    try:
        response = client.send_email(
            Destination={
                'ToAddresses': [
                    recipient,
                ],
            },
            Message={
                'Body': {
                    'Text': {
                        'Charset': CHARSET,
                        'Data': body,
                    },
                },
                'Subject': {
                    'Charset': CHARSET,
                    'Data': SUBJECT,
                },
            },
            Source=SENDER,
        )
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print("Email sent! Message ID:"),
        print(response['MessageId'])

send_email("recipient@example.com", response)
