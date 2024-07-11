from google.cloud import bigquery
from dotenv import load_dotenv
import logging
from big_utils import create_dataset
import json


logging.basicConfig(level=logging.INFO, format="%(asctime)s:%(levelname)s:%(message)s")

load_dotenv()

PROJECT_ID = "pygcs-425623"
DATASET_ID = "etl_intro"
TABLE_ID = "fake_bank"

logging.info("Testing logger!!")

client = bigquery.Client(project=PROJECT_ID)

# Dataset creation

# dataset_ref = client.dataset(DATASET_ID)
# dataset = client.create_dataset(dataset_ref)

create_dataset(client=client, dataset_id=DATASET_ID)

logging.info(f"Dataset {DATASET_ID} created successfully!")


# table creation using schema
# schema = [
#     bigquery.SchemaField("transactionDate", "STRING", mode="REQUIRED"),
#     bigquery.SchemaField("description", "STRING", mode="REQUIRED"),
#     bigquery.SchemaField("category", "STRING", mode="REQUIRED"),
#     bigquery.SchemaField("debit", "float64", mode="NULLABLE"),
#     bigquery.SchemaField("credit", "float64", mode="NULLABLE"),
#     bigquery.SchemaField("id", "INTEGER", mode="REQUIRED")
# ]


# table creation using json
with open('schema.json', 'r') as f:
    metadata = f.read()
    schema = json.loads(metadata)

table_ref = "pygcs-425623.etl_intro.bank_transaction_v3"
table = bigquery.Table(table_ref, schema=schema)
client.create_table(table)

logging.info("Table created successfully!")

# table creation usin sql ddl
# ddl = """
# CREATE TABLE `pygcs-425623.etl_intro.bank_transaction` (
#     id int64,
#     category string,
#     description string,
#     debit float64,
#     credit float64,
#     transactionDate string
# )
# """
# query_job = client.query(ddl)

# query_job.result()

logging.info("Table created successfully!")