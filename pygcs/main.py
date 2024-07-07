import requests
from gcs_manager import GCSManager
import json
from io import StringIO
import constants
from api import fetch_play_station_data, stringify



# url = "https://api.sampleapis.com/playstation/games"


if __name__ == "__main__":
    manager = GCSManager(project_id="pygcs-425623")
    api_data = fetch_play_station_data
    api_data_buffer = stringify(api_data)
    manager.upload_file(constants.ETL_BUCKET, blob_name="clean_etl", bucket=api_data)




# def write_to_gcs_bucket(client, bucket, file_name, file_buffer, content_type="application/json"):

#     bucket = client.bucket(bucket)
#     blob = bucket.blob(file_name)
#     data_types = file_buffer.getvalue().encode("utf-8")
#     blob.upload_from_string(data_types, content_type=content_type)
#     print(f"Successfully wrote data to {file_name}")
#     return f"gs://{bucket}/{file_name}"


# # create bucket
# manager = GCSManager(project_id="pygcs-425623")

# # manager.create_bucket(bucket_name="etl_basic")


# response = requests.get(url)

# response.raise_for_status()

# data = response.json()

# file_name = "play_station.json"

# io_string = StringIO(json.dumps(data))

# io_string.seek(0)

# write_to_gcs_bucket(client=manager.client, bucket="etl_basic", file_name="auto_play_station_load.json", file_buffer=io_string)

# print(data[0])


# write a file to local then upload to gcs bucket

# with open(file_name, "w") as f:
#     json.dump(data, f) 

# bucket = manager.client.bucket("etl_basic")
# blob = bucket.blob(file_name)
# blob.upload_from_filename(file_name)    


# assert isinstance(data, list), "Expected an array of json!"

# print("Success!")


            
               


