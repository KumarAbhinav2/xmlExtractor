import csv
from xmlExtractor.settings import CSVConstants as cconst
import boto3

class CSVHandler:

    def __init__(self, outfile):
        self.outfile = outfile
        self.handle = self._create_file()
        self.s3 = boto3.client('s3')

    def _create_file(self):
        data = open(self.outfile, 'w', newline='', encoding='utf-8')
        csvwriter = csv.writer(data)
        csvwriter.writerow(cconst.cols)
        return csvwriter

    # @contextmanager
    # def csv_writer(self, bucket, key, **kwargs):
    #     """Wrapper around csv.writer for writing large csv files to s3 object.
    #     Leverages a TemporaryFile to not have to hold CSV content in memory, and
    #     uses s3 upload_fileobj method to do a multipart upload of the large file to S3.
    #     Args: bucket (str): S3 Bucket Name.
    #     key (str): S3 Object Key.
    #     **kwargs: Keyword arguments to pass along to the underlying csv writer implementation.
    #     Yields: csv.writer: """
    #     with TemporaryFile("wb+") as fp:
    #         with io.TextIOWrapper(fp, encoding="utf-8", newline="") as buf:
    #             yield csv.writer(buf, **kwargs)
    #             buf.flush()
    #             buf.seek(0)
    #             self.s3.Object(bucket, key).upload_fileobj(fp)

    def get_handle(self):
        return self.handle