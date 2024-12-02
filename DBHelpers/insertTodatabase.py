import json
import os
import datetime
from pymongo import MongoClient
from Utilities.deserialize import deserialize_data
from dotenv import load_dotenv

load_dotenv()

def insert_data():
    client = MongoClient(os.getenv("DATABASE_URL"))
    db = client[os.getenv("DATABASE_NAME")]
    collection_name = db[os.getenv("COLLECTION_NAME")]

    data = deserialize_data(os.getenv("TRAINING_PATH"))
    
    collection_name.insert_many(data)
    print(f"{len(data)} documents inserted successfully!")

if __name__ == "__main__":
    insert_data()
