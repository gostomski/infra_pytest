import string 
import random 

import time
import requests
import os

#import pytest

import logging
import boto3
from botocore.exceptions import ClientError

class TestClass:
    def setup_class(self):
        self.file_name = "test_s3_upload_" + self.random_generator(6)
 
    def random_generator(self, size=6):
        return ''.join(random.choices(string.ascii_lowercase + string.digits, k = size  )) 
    

    def upload_file(self, file_name, bucket, object_name=None):
        """Upload a file to an S3 bucket

        :param file_name: File to upload
        :param bucket: Bucket to upload to
        :param object_name: S3 object name. If not specified then file_name is used
        :return: True if file was uploaded, else False
        """

        # If S3 object_name was not specified, use file_name
        if object_name is None:
            object_name = file_name

        # Upload the file
        s3_client = boto3.client('s3')
        try:
            response = s3_client.upload_file(file_name, bucket, object_name)
        except ClientError as e:
            logging.error(e)
            return False
        return True



    def test_s3_upoad_file_equals_true(self, variables):
        f = open("%s.txt" % self.file_name, "a")
        f.write("Now the file has more content!")
        f.close()
        r = self.upload_file("%s.txt" % self.file_name, variables['s3_bucket'])
        os.remove("%s.txt" % self.file_name)
        assert r == True

    def test_cloudfront_response_status_code_equals_200(self, variables):
        r = requests.get("%s/%s.txt" % (variables['cloudfront_url'], self.file_name))
        assert r.status_code == 200
        time.sleep(1) # sleep for 1 second

    def test_cloudfront_response_status_code_equals_404(self, variables):
        r = requests.get("%s/%s.txt" % (variables['cloudfront_url'], self.file_name))
        assert r.status_code == 404
