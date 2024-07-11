from google.cloud import bigquery
from google.cloud.exceptions import NotFound, Conflict
from dotenv import load_dotenv
import logging
import json

logging.basicConfig(level=logging.INFO, format="%(asctime)s:%(levelname)s:%(message)s")


PROJECT_ID = "pygcs-425623"
DATASET_ID = "etl_intro"
TABLE_ID = "fake_bank"

load_dotenv()


# making the code idempotent

def create_dataset(client:bigquery.Client, dataset_id:str)-> None:
    try:
        dataset_ref = client.dataset(DATASET_ID)
        client.create_dataset(dataset_ref)
        logging.info(f"Dataset {dataset_id} created successfully!")
    except Conflict:
        logging.info("Dataset already exists, exiting as successful!")    
    except Exception as e:
        logging.error(f"Encountered issue creating the Dataset {dataset_id}: {e}") 
        raise e   

def create_table(client:bigquery.Client, project_id:str, dataset_id:str, table_id:str, schema_path:str)-> None:
    # locate schema / read schema
    try:
        logging.info(f"Reading schema from {schema_path}")
        with open(schema_path, 'r') as f:
            schema_json = json.load(f)
            logging.info(f"Schema: {schema_json}")

    # Ensure schema is a list of dictionaries
        if not isinstance(schema_json, list):
            raise ValueError("Schema should be a list of dictionaries.")

        # Convert schema to BigQuery SchemaField format
        bq_schema = [bigquery.SchemaField.from_api_repr(field) for field in schema_json]
        logging.info(f"Converted BigQuery Schema: {bq_schema}")

        table_ref = f"{project_id}.{dataset_id}.{table_id}"
        table = bigquery.Table(table_ref, schema=bq_schema)
        # client.create_table(table)

        client.create_table(table, exists_ok=True)
        logging.info(f"Table {table_id} created or already exists.")

    except Conflict:
        logging.info(f"Table {table_id} already exists, skipping creation.")    
    except Exception as e:
        logging.error(f"Encountered issue creating the Table {table_id}: {e}") 
        raise e     
