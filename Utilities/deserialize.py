import datetime
import json

def deserialize_data(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
        for document in data:
            if "timestamp" in document:
                document["timestamp"] = datetime.datetime.fromisoformat(document["timestamp"])
    return data