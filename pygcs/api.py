import requests
import json
from io import StringIO
import constants

# url = "https://api.sampleapis.com/playstation/games"

url = f"{constants.PLAY_BASE_URL}/{constants.ACCOUNTS_ENDPOINT}"


def fetch_play_station_data():
    response = requests.get(url)

    response.raise_for_status()

    data = response.json()
    return data


def stringify(data):
    io_string = StringIO(json.dumps(data))

    io_string.seek(0)
    return io_string