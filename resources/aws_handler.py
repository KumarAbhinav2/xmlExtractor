import boto3
from xmlExtractor.settings import AWSConstants as aconst

class AWSManager:

    def __init__(self, bucket):
        self.bucket = aconst.bucket

    def upload_file(self, filename):
        """
        Uploads file to a S3 bucket
        """
        obj = filename
        s3_client = boto3.client('s3')
        return s3_client.upload_file(filename, self.bucket, obj)