import boto3

class AwsKmsService:
    def __init__(self, endpoint_url):
        self.kms = boto3.client('kms', endpoint_url=endpoint_url) #TODO add the acutal endpoint

    def create_new_key(self):
        response = self.kms.create_key()
        return response['KeyMetadata']['KeyId']