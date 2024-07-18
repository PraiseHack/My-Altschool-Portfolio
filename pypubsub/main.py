from dotenv import load_dotenv
import os
from google.cloud import pubsub_v1
from faker import Faker
import json
import time


# Load environment variables from a .env file
load_dotenv()

# Initialize Faker for generating fake data
fake = Faker()

# Define Google Cloud project ID and Pub/Sub topic ID
project_id = 'pygcs-425623'
topic_id = 'alt-topic'

# Initialize the Pub/Sub publisher client
publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(project_id, topic_id)


def generate_fake_user_data():

    """Generate fake user data."""
    return{
        "name": fake.name(),
        "address": fake.address(),
        "email": fake.email(),
        "phone_number": fake.phone_number(),
        "birthdate": fake.date_of_birth().isoformat(),
        "created_at": fake.date_time_this_year().isoformat()
    }


def publish_message(data):
    """Publish a message to the Pub/Sub topic."""
    try:
        # convert data to json string
        data_str = json.dumps(data)
        # data must be a bytestring
        data_bytes = data_str.encode("utf-8")

        # publish the message
        future = publisher.publish(topic_path, data_bytes)
        print(f"Published message ID: {future.result()}")
    except Exception as e:
        print(f"An error occurred while publishing message: {e}")
    

def main():
    """Main function to generate and publish fake user data continuously."""
    try:
        while True:
            user_data = generate_fake_user_data()
            publish_message(user_data)
            time.sleep(5)
    except KeyboardInterrupt:
        print("Stopping the data generator.")
    

if __name__ == "__main__":
    main()        