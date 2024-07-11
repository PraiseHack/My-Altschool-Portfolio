from msilib import Table
import sched
from google.cloud import bigquery
from dotenv import load_dotenv
import logging
from big_utils import create_dataset, create_table
import json
import requests


logging.basicConfig(level=logging.INFO, format="%(asctime)s-%(levelname)s-%(message)s")

load_dotenv()

PROJECT_ID = "pygcs-425623"
DATASET_ID = "etl_intro"
TABLE_ID = "fake_bank_transactions"
SCHEMA_PATH = r".\schema.json"
BASE_URL = "https://api.sampleapis.com/fakebank/"
TARGET_ENDPOINT = "accounts"

logging.info("Testing logger!!")

client = bigquery.Client(project=PROJECT_ID)

# create dataset

create_dataset(client=client, dataset_id=DATASET_ID)

logging.info(f"Dataset {DATASET_ID} created successfully!")

# create table

create_table(client=client, project_id=PROJECT_ID, dataset_id=DATASET_ID, table_id=TABLE_ID, schema_path=SCHEMA_PATH)

# load data
# with open("schema.json", 'r') as f:
#     schema_json = json.load(f)

# Convert schema to BigQuery SchemaField objects
# schema = [bigquery.SchemaField.from_api_repr(field) for field in schema_json]

table_ref = f"{PROJECT_ID}.{DATASET_ID}.{TABLE_ID}"
# table = bigquery.Table(table_ref, schema=schema_json)
# table = client.create_table(table, exists_ok=True)  # This returns the created table

# logging.info("Table created successfully!")

# extract the data from source
response = requests.get(f"{BASE_URL}/{TARGET_ENDPOINT}")
response.raise_for_status()
data = response.json()

# load the data into table
# logging.info(f"Data: {data}")

# insert the data
errors = client.insert_rows_json(table_ref, data)  # Use insert_rows_json for JSON data

if errors == []:
    logging.info("New rows have been added.")
else:
    logging.info(f"Encountered errors while inserting rows: {errors}")    