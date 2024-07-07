from main import GCSManager

manager = GCSManager()

manager.list_gcs_buckets()


from google.cloud import storage
from dotenv import load_dotenv
from google.cloud import bigquery
import os

load_dotenv()


GOOGLE_APPLICATION_CREDENTIALS = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")
# Ensure the variable is set correctly
if GOOGLE_APPLICATION_CREDENTIALS is None:
    raise ValueError("GOOGLE_APPLICATION_CREDENTIALS environment variable is not set")
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = GOOGLE_APPLICATION_CREDENTIALS

# create client
gcs_client = storage.Client()

for bucket in gcs_client.list_buckets():
    print(bucket)

# create bucket
BUCKET_NAME = "play-station1"
location = "europe-west1"
storage_class = "STANDARD"

# bucket = gcs_client.bucket(BUCKET_NAME)
# bucket.storage_class = storage_class
# bucket.location = location
# bucket.create()

# print("bucket ceated successfully!")


# upload local file to a gcs bucket

# file_path = r"..\postgres_docker_init\data\TSLA.csv"
# blob_name = "tesla_trades.csv"
# bucket = gcs_client.bucket(BUCKET_NAME)
# blob = bucket.blob(blob_name)
# blob.upload_from_filename(filename=file_path)

# list objects in a bucket

# for obj in gcs_client.list_blobs(BUCKET_NAME):
#     print(obj.name)


# downlaod a file from a bucket
blob_name = "tesla_trades.csv"
destination_path = r"data\tesla.csv"
bucket = gcs_client.bucket(BUCKET_NAME)
blob = bucket.blob(blob_name)
blob.download_to_filename(destination_path)