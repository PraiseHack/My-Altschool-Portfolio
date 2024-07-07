from google.cloud import storage
import os
from dotenv import load_dotenv

load_dotenv()

class GCSManager:
    def __init__(self, project_id) -> None:
        self.project_id = project_id
        self.client = self._start_gcs_client()

    def _start_gcs_client(self):
        return storage.Client(project=self.project_id)   

    def list_gcs_buckets(self):
        for bucket in self.client.list_buckets():
            print(bucket.name) 

    def create_bucket(self, bucket_name, storage_class = "STANDARD", location = "europe-west1"):
        bucket = self.client.bucket(bucket_name)
        bucket.storage_class = storage_class
        bucket.location = location
        bucket.create()

        print(f"{bucket_name}bucket ceated successfully!")

    def upload_file(self, bucket:str, blob_name:str, local_path:str = None, buffer = None, content_type="application/json"):
        bucket = self.client.bucket(bucket)
        if buffer:
            blob = bucket.blob(blob_name)
            data_types = buffer.getvalue().encode("utf-8")
            blob.upload_from_string(data_types, content_type=content_type)
        else:
            blob = bucket.blob(blob_name)
            blob.upload_from_filename(local_path)
            