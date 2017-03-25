import boto3
import botocore

import time

from botocore.exceptions import ClientError
from CredentialProviderWrapper import CredentialProviderWrapper


class CloudWatchLogsWrapper:

    def __init__(self, sequenceToken):
        credentials = CredentialProviderWrapper()
        session = credentials.getProviderFromAssumeRole()
        self.client = session.client('logs')

        self.sequenceToken = sequenceToken
        self.retries = 0

    def putLogEvents(self, message, logGroupName, logStreamName):
        timestamp = int(time.time()) * 1000

        print "\nSending Message to CloudWatch {0}".format(message)

        try:
            response = self.client.put_log_events(
                logGroupName=logGroupName,
                logStreamName=logStreamName,
                logEvents=[
                    {
                        'timestamp': timestamp,
                        'message': message
                    },
                ],
                sequenceToken=self.sequenceToken
            )
        except ClientError as err:
            dir(err)
            # err = err.getMessage()
            # token = err[err.find('sequenceToken: ') + 1:-1]
            # print("OS error: {0}".format(token))

    def describeLogsStreams(self, logGroupName):
        response = self.client.describe_log_streams(
            logGroupName=logGroupName,
        )
        return response

client = CloudWatchLogsWrapper('49571399552294708856423929684273112390670778100017537570');

result = client.putLogEvents("Hello from boto2", '/var/log/httpd/access', 'sandbox-log-stream')
result2 = client.describeLogsStreams('/var/log/httpd/access')

print result2