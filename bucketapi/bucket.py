from bucketapi.params import *
import pandas as pd
from google.cloud import storage
import os
import io
from io import BytesIO

class Getbucket():
    def __init__(self):
        # Connect to the database
        self.client = storage.Client()

    def post(self,filename, data):

        df = pd.read_json(data)

        bucket = self.client.get_bucket(BUCKET_NAME)

        blob = bucket.blob(f"{BUCKET_DATA_PATH}{filename}")

        df.to_csv(filename, index=False)

        with open(filename, 'rb') as f:
            blob.upload_from_file(f)

        if os.path.exists(filename):
            os.remove(filename)
        else:
            return {'result': f"{filename} error"}

        return {'result': f"{filename} inserted in the bucket {BUCKET_NAME}"}

    def get(self, filename, nrows=None, **kwargs):

        path = f"gs://{BUCKET_NAME}/{BUCKET_FOLDER}/{filename}"

        df = pd.read_csv(path, nrows=nrows)

        return df.to_json()
