import boto3


class CredentialProviderWrapper:

    def __init__(self):
        self.client = boto3.client('sts')

    def getProviderFromAssumeRole(self):
        response = self.client.assume_role(
            DurationSeconds=3600,
            RoleArn='arn:aws:iam::000000000000:role/YourRole',
            RoleSessionName='PythonAwsWrapper',
        )

        session = boto3.Session(
            aws_access_key_id=response['Credentials']['AccessKeyId'],
            aws_secret_access_key=response['Credentials']['SecretAccessKey'],
            aws_session_token=response['Credentials']['SessionToken'],
            region_name='eu-west-1'
        )

        return session